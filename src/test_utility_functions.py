import unittest
import re
from textnode import TextType,TextNode
from utility_functions import split_nodes_delimiter


class TestSplitNodes(unittest.TestCase):
    def test_split_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

    def test_repeated_delimiters(self):
        node = TextNode("This is **a bold phrase** and this is **another bold phrase**. This is very cool.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("a bold phrase", TextType.BOLD),
            TextNode(" and this is ", TextType.TEXT),
            TextNode("another bold phrase", TextType.BOLD),
            TextNode(". This is very cool.", TextType.TEXT),
        ])

    def test_repeated_delimiters_empty_string(self):
        node = TextNode("This is **a bold phrase****another bold phrase**. This is very cool.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("a bold phrase", TextType.BOLD),
            TextNode("another bold phrase", TextType.BOLD),
            TextNode(". This is very cool.", TextType.TEXT),
        ])

    def test_split_code_block_multiple_words(self):
        node = TextNode("This is text with a `this is a code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("this is a code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

    def test_repeated_letters(self):
        node = TextNode("A A `A`A A", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("A A ", TextType.TEXT),
            TextNode("A", TextType.CODE),
            TextNode("A A", TextType.TEXT),
        ])

    def test_no_closing_delimiter(self):
        node = TextNode("This is text with a `code block word", TextType.TEXT)
        delimiter = "`"
        expected_msg = f"Closing {delimiter} was not found in 'This is text with a `code block word'"
        with self.assertRaisesRegex(ValueError, re.escape(expected_msg)):
            split_nodes_delimiter([node], delimiter, TextType.CODE)

    def test_no_closing_delimiter_after_normal_delimiter(self):
        node = TextNode("This is **a bold phrase** and this is **another bold phrase.", TextType.TEXT)
        delimiter = "**"
        expected_msg = f"Closing {delimiter} was not found in ' and this is **another bold phrase.'"
        with self.assertRaisesRegex(ValueError, re.escape(expected_msg)):
            split_nodes_delimiter([node], delimiter, TextType.BOLD)

    def test_mixed_delimiters(self):
        node = TextNode("This is **bold** text with a `hello world code block` word and an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is **bold** text with a ", TextType.TEXT),
            TextNode("hello world code block", TextType.CODE),
            TextNode(" word and an _italic_ word", TextType.TEXT),
        ])
        new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text with a ", TextType.TEXT),
            TextNode("hello world code block", TextType.CODE),
            TextNode(" word and an _italic_ word", TextType.TEXT),
        ])
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text with a ", TextType.TEXT),
            TextNode("hello world code block", TextType.CODE),
            TextNode(" word and an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT)
        ])

    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )