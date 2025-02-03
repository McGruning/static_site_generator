import re


def extract_markdown_images(text):
    
    """
    Extracts image tags from markdown text and returns a list of tuples.
    Each tuple contains the alt text and the image URL.

    :param text: The markdown text to extract images from
    :return: A list of tuples
    """
    # Find all image tags in the text
    image_tags = re.findall(r"!\[([^\]]*)\]\(([^)]*)\)", text)
    # Return a list of tuples containing the alt text and image URL
    return image_tags

def extract_markdown_links(text):

    """
    Extracts link tags from markdown text and returns a list of tuples.
    Each tuple contains the link text and the link URL.

    :param text: The markdown text to extract links from
    :return: A list of tuples
    """
    # Find all link tags in the text
    link_tags = re.findall(r"\[([^\]]*)\]\(([^)]*)\)", text)
    # Return a list of tuples containing the link text and link URL
    return link_tags