from .GenericDocument import GenericDocument


class PlainDocument(GenericDocument):
    def render_paragraph(self, text) -> str:
        text = text + "\n\n"
        return text
