from textnode import TextNode, TextType

def main():
    node1 = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node1)
    node2 = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node1 == "node2")

main()