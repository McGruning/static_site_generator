import unittest
from markdown import extract_markdown_images, extract_markdown_links

class TestMarkdownFunctions(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "Here is an image ![alt text](http://example.com/image.jpg) in markdown."
        expected = [("alt text", "http://example.com/image.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)

        text = "Multiple images ![first](http://example.com/first.jpg) and ![second](http://example.com/second.jpg)."
        expected = [("first", "http://example.com/first.jpg"), ("second", "http://example.com/second.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)

        text = "No images here."
        expected = []
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_links(self):
        text = "Here is a link [link text](http://example.com) in markdown."
        expected = [("link text", "http://example.com")]
        self.assertEqual(extract_markdown_links(text), expected)

        text = "Multiple links [first](http://example.com/first) and [second](http://example.com/second)."
        expected = [("first", "http://example.com/first"), ("second", "http://example.com/second")]
        self.assertEqual(extract_markdown_links(text), expected)

        text = "No links here."
        expected = []
        self.assertEqual(extract_markdown_links(text), expected)

if __name__ == "__main__":
    unittest.main()