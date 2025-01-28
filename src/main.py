from textnode import TextNode, TextType

def main():
    # Create a test node with some sample values
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

if __name__ == "__main__":
    main()