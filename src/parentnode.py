from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag in parent node!")
        if self.children is None or len(self.children) == 0:
            raise ValueError("No childern in parent node!")
        childern_to_html = ""
        for child in self.children:
            childern_to_html += child.to_html()

        return f"<{self.tag}>{self.props_to_html()}{childern_to_html}</{self.tag}>"