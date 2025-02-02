import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        # Case 1: Test with no properties
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")

        # Case 2: Single key-value pair
        node = HTMLNode(props={"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')

        # Case 3: Multiple key-value pairs
        node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com" target="_blank"')

class TestParentNode(unittest.TestCase):
    def test_initialization(self):
        with self.assertRaises(ValueError):
            ParentNode(tag=None, children=[HTMLNode(tag="div")])
        with self.assertRaises(ValueError):
            ParentNode(tag="", children=[HTMLNode(tag="div")])
        with self.assertRaises(ValueError):
            ParentNode(tag="div", children=None)
        with self.assertRaises(ValueError):
            ParentNode(tag="div", children=[])

        # Valid initialization
        node = ParentNode(tag="div", children=[HTMLNode(tag="span")])
        self.assertEqual(node.tag, "div")
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.children[0].tag, "span")

    def test_to_html(self):
        child1 = LeafNode(tag="span", value="Hello")
        child2 = LeafNode(tag="span", value="World")
        parent = ParentNode(tag="div", children=[child1, child2])
        expected_html = '<div><span>Hello</span><span>World</span></div>'
        self.assertEqual(parent.to_html(), expected_html)



if __name__ == "__main__":
    unittest.main()