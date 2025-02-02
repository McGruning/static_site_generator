class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def props_to_html(self):
        # a space-separated string of HTML attributes
        if self.props is None:
            return ""
        return " " + " ".join([f'{key}="{value}"' for key, value in self.props.items()])

    def to_html(self):
        raise NotImplementedError

    def __repr__(self):
        if self.children is None:
            children_repr = "None"
        else:
            # List the tag for each child node, or 'None' if the child has no tag
            children_repr = f"[{', '.join(child.tag or 'None' for child in self.children)}]"
        return f"HTMLNode({self.tag}, {self.value}, {children_repr}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)
        self._children = None

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None or self.tag == "":
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None or tag == "":
            raise ValueError("ParentNode must have a tag")
        if children is None:
            raise ValueError("ParentNode must have children")
        if isinstance(children, list) and len(children) == 0:
            raise ValueError("Children cannot be an empty list")
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"