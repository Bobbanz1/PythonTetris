from .GenericDocument import GenericDocument


class MarkdownDocument(GenericDocument):
    @classmethod
    def escape_markdown(cls, text):
        return text.replace("\\", "\\\\").replace("`", "\\`").replace("#", "\\#")

    def render_heading1(self, text) -> str:
        stringy = str(text)
        stringy = MarkdownDocument.escape_markdown(stringy)
        breakline = stringy.replace("\n", " ")
        output_text = "# " + breakline + "\n\n"
        return output_text

    def render_heading2(self, text) -> str:
        stringy = str(text)
        stringy = MarkdownDocument.escape_markdown(stringy)
        breakline = stringy.replace("\n", " ")
        output_text = "## " + breakline + "\n\n"
        return output_text

    def render_heading3(self, text) -> str:
        stringy = str(text)
        stringy = MarkdownDocument.escape_markdown(stringy)
        breakline = stringy.replace("\n", " ")
        output_text = "### " + breakline + "\n\n"
        return output_text

    def render_paragraph(self, text) -> str:
        stringy = str(text)
        stringy = MarkdownDocument.escape_markdown(stringy)
        output_text = stringy + "\n\n"
        return output_text

    def render_codeblock(self, text) -> str:
        stringy = str(text)
        stringy = MarkdownDocument.escape_markdown(stringy)
        output_text = "```\n" + stringy + "\n```\n\n"
        return output_text
