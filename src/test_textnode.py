import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_nodes_without_link(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_eq_nodes_with_link(self):
        node1 = TextNode("This is a text node", TextType.BOLD, url="www.testlink.com")
        node2 = TextNode("This is a text node", TextType.BOLD, url="www.testlink.com")
        self.assertEqual(node1, node2)
    
    def test_non_eq_nodes_text(self):
        node1 = TextNode("Test string 1", TextType.BOLD)
        node2 = TextNode("Test string 2", TextType.BOLD)
        self.assertNotEqual(node1, node2)
    
    def test_non_eq_nodes_text_type(self):
        node1 = TextNode("Test string 1", TextType.LINK)
        node2 = TextNode("Test string 1", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_non_eq_nodes_URL(self):
        node1 = TextNode("Test string 1", TextType.LINK, url="www.testlink1.com")
        node2 = TextNode("Test string 1", TextType.LINK, url="www.testlink2.com")
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()