from textnode import TextType,TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text_to_split = node.text
        if delimiter not in text_to_split:
            new_nodes.append(TextNode(text_to_split, TextType.TEXT))
            continue
        splitted = text_to_split.split(delimiter, 2)
        if len(splitted) < 3:
            raise ValueError(f"Closing {delimiter} was not found in '{text_to_split}'")
        if splitted[0] != "":
            new_nodes.append(TextNode(splitted[0], TextType.TEXT))
        if splitted[1] != "":
            new_nodes.append(TextNode(splitted[1], text_type))
        if splitted[2] != "":
            if delimiter in splitted[2]:
                old_nodes.append(TextNode(splitted[2], TextType.TEXT))
            else:
                new_nodes.append(TextNode(splitted[2], TextType.TEXT))
    return new_nodes