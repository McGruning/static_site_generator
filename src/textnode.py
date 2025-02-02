from enum import Enum

from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(tag=None, value=text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    if text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)
    if text_node.text_type == TextType.IMAGE:
        return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unsupported text type: {text_node.text_type}")

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    LINK = "link"
    CODE = "code"
    IMAGE = "image"


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        # comares all properties of the object
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    
    def __repr__(self):
        # returns a string representation of the object
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

