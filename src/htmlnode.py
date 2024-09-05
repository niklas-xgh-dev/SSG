class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        
        props_html = " ".join(f'{key}="{value}"' for key, value in self.props.items())
        return f" {props_html}"
    
    def __repr__(self):
        attributes = []
        if self.tag is not None:
            attributes.append(f"Tag:{self.tag}")
        if self.value is not None:
            attributes.append(f"value:{self.value}")
        if self.children is not None:
            attributes.append(f"children:{self.children}")
        if self.props is not None:
            attributes.append(f"props:{self.props}")
        
        return " ".join(attributes)