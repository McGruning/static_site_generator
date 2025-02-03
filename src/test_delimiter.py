import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_single_node_single_delimiter(self):
        old_nodes = [TextNode("Hello,World", TextType.TEXT)]
        delimiter = ","
        text_type = TextType.BOLD
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes[0].text, "Hello")
        self.assertEqual(new_nodes[0].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[1].text, ",World")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)

    def test_multiple_nodes_single_delimiter(self):
        old_nodes = [TextNode("Hello,World", TextType.TEXT), TextNode("Foo,Bar", TextType.TEXT)]
        delimiter = ","
        text_type = TextType.ITALIC
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0].text, "Hello")
        self.assertEqual(new_nodes[0].text_type, TextType.ITALIC)
        self.assertEqual(new_nodes[1].text, ",World")
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(new_nodes[2].text, "Foo")
        self.assertEqual(new_nodes[2].text_type, TextType.ITALIC)
        self.assertEqual(new_nodes[3].text, ",Bar")
        self.assertEqual(new_nodes[3].text_type, TextType.ITALIC)

    def test_single_node_multiple_delimiters(self):
        old_nodes = [TextNode("Hello,World,Again", TextType.TEXT)]
        delimiter = ","
        text_type = TextType.LINK
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "Hello")
        self.assertEqual(new_nodes[0].text_type, TextType.LINK)
        self.assertEqual(new_nodes[1].text, ",World")
        self.assertEqual(new_nodes[1].text_type, TextType.LINK)
        self.assertEqual(new_nodes[2].text, ",Again")
        self.assertEqual(new_nodes[2].text_type, TextType.LINK)

    def test_single_node_no_delimiter(self):
        old_nodes = [TextNode("HelloWorld", TextType.TEXT)]
        delimiter = ","
        text_type = TextType.CODE
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "HelloWorld")
        self.assertEqual(new_nodes[0].text_type, TextType.CODE)

    def test_empty_list(self):
        old_nodes = []
        delimiter = ","
        text_type = TextType.BOLD
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(len(new_nodes), 0)

if __name__ == "__main__":
    unittest.main()