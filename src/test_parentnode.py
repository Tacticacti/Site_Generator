import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_single_child(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_more_than_one_children(self):
        child_node1 = LeafNode("span", "child1")
        child_node2 = LeafNode("b", "child2")
        parent_node = ParentNode("div", [child_node1,child_node2])
        self.assertEqual(parent_node.to_html(), "<div><span>child1</span><b>child2</b></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_grandchildren_more_than_one_child(self):
        child_node1 = LeafNode("span", "child1")
        child_node2 = LeafNode("b", "child2")
        parent_node1 = ParentNode("div", [child_node1,child_node2])
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node2 = ParentNode("div", [child_node])
        parent_node = ParentNode("div", [parent_node1, parent_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><div><span>child1</span><b>child2</b></div><div><span><b>grandchild</b></span></div></div>",
        )

    def test_to_html_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaisesRegex(ValueError, "No tag in parent node!"):
            parent_node.to_html()

    def test_to_html_children_is_none(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("p", None)
        with self.assertRaisesRegex(ValueError, "No childern in parent node!"):
            parent_node.to_html()

    def test_to_html_no_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(tag="p", children=[])
        with self.assertRaisesRegex(ValueError, "No childern in parent node!"):
            parent_node.to_html()

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )