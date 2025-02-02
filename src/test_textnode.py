import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_node(self):
        text_node = TextNode(text="Hello", text_type=TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "Hello")

    def test_bold_node(self):
        text_node = TextNode(text="Bold Text", text_type=TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold Text")

    def test_italic_node(self):
        text_node = TextNode(text="Italic Text", text_type=TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic Text")

    def test_link_node(self):
        text_node = TextNode(text="Link Text", text_type=TextType.LINK, url="https://example.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Link Text")
        self.assertEqual(html_node.props, {"href": "https://example.com"})

    def test_code_node(self):
        text_node = TextNode(text="Code Text", text_type=TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Code Text")

    def test_image_node(self):
        text_node = TextNode(text="Image Alt", text_type=TextType.IMAGE, url="https://example.com/image.png")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://example.com/image.png", "alt": "Image Alt"})

    def test_unsupported_node(self):
        text_node = TextNode(text="Unsupported", text_type="unsupported")
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)



if __name__ == "__main__":
    unittest.main()