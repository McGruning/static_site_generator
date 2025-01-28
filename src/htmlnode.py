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