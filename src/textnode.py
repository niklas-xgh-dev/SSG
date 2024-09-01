class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, obj):
        return self.text == obj.text and self.text_type == obj.text_type and self.url ==obj.url

    def __repr__(self):
        returnstr = f"TextNode ({self.text}, {self.text_type}, {self.url})"
        return returnstr
    

    