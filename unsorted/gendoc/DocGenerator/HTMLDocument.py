from .GenericDocument import GenericDocument


class HTMLDocument(GenericDocument):

    @classmethod
    def escape_html(cls, text):
        return (
            text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#39;")
        )

    def render_heading1(self, text) -> str:
        stringy = str(text)
        stringy = HTMLDocument.escape_html(stringy)
        breakline = stringy.replace("\n", "<br>")
        output_text = "<h1>" + breakline + "</h1>"
        return output_text

    def render_heading2(self, text) -> str:
        stringy = str(text)
        stringy = HTMLDocument.escape_html(stringy)
        breakline = stringy.replace("\n", "<br>")
        output_text = "<h2>" + breakline + "</h2>"
        return output_text

    def render_heading3(self, text) -> str:
        stringy = str(text)
        stringy = HTMLDocument.escape_html(stringy)
        breakline = stringy.replace("\n", "<br>")
        output_text = "<h3>" + breakline + "</h3>"
        return output_text

    def render_paragraph(self, text) -> str:
        stringy = str(text)
        stringy = HTMLDocument.escape_html(stringy)
        breakline = stringy.replace("\n", "<br>")
        output_text = "<p>" + breakline + "</p>"
        return output_text

    def render_codeblock(self, text) -> str:
        stringy = str(text)
        stringy = HTMLDocument.escape_html(stringy)
        output_text = "<pre><code>" + stringy + "</code></pre>"
        return output_text
