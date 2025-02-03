from textnode import TextNode, TextType
from htmlnode import HTMLNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    Split a list of TextNodes by a delimiter and apply a text type to each node.

    :param old_nodes: The list of TextNodes to split
    :param delimiter: The delimiter to split the nodes by
    :param text_type: The text type to apply to each node
    :return: A list of TextNodes
    """
    new_nodes = []
    for node in old_nodes:
        parts = node.text.split(delimiter)
        for i, part in enumerate(parts):
            new_node = TextNode(part, text_type, node.url)
            if i == 0:
                new_node.text = part
            else:
                new_node.text = delimiter + part
            new_nodes.append(new_node)
    return new_nodes


if __name__ == "__main__":
    main()