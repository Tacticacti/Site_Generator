import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p_no_prop(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.__repr__(),"LeafNode(tag=p, value=Hello, world!, props=None)")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p")
        self.assertEqual(node.__repr__(),"LeafNode(tag=p, value=None, props=None)")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(value="hello world!")
        self.assertEqual(node.__repr__(),"LeafNode(tag=None, value=hello world!, props=None)")
        self.assertEqual(node.to_html(), "hello world!")

    def test_leaf_to_html_p_with_prop(self):
        node = LeafNode("p", "Hello, world!", {"class": "greeting", "href": "https://boot.dev"})
        self.assertEqual(node.__repr__(),"LeafNode(tag=p, value=Hello, world!, props={'class': 'greeting', 'href': 'https://boot.dev'})")
        self.assertEqual(node.to_html(), '<p class="greeting" href="https://boot.dev">Hello, world!</p>')