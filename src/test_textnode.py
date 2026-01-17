import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(node, node2)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")


if __name__ == "__main__":
    unittest.main()