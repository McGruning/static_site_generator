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
    def __init__(self, tag, value,  props=None):
        super().__init__(tag, value, props=props)
        if  self.children is not None:
            raise AttributeError("LeafNode cannot have children")
        self.children = None

    @property    
    def children(self):
        return None
    
    @children.setter
    def children(self, _):
        raise AttributeError("LeafNode cannot have children")

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None or self.tag == "":
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"