class HTMLNode:
    def __init__(self, tag, value, children, props) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        pass

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_html = f"
        {
        'href': '{self.props}', 
        'target': '_blank',
        }
        "
        return