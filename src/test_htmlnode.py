import unittest

from htmlnode import HTMLNode


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
       



if __name__ == "__main__":
    unittest.main()