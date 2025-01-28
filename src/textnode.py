from enum import Enum

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

