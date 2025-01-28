import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        # Testing equality of two identical nodes
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_text_type(self):
        # Testing inequality based on TextType difference
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, TextNode("This is a text node", TextType.ITALIC))

    def test_not_eq_url(self):
        # Testing inequality based on URL property
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev"))



if __name__ == "__main__":
    unittest.main()