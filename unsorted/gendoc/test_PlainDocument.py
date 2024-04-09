from .DocGenerator.PlainDocument import PlainDocument


def test_render_small_heading3():
    doc = PlainDocument()
    doc.add_heading3("Heading 3")
    expecting = "Heading 3\n\n"
    rendered = doc.render()
    rendered = ''.join(rendered)
    assert rendered == expecting

def test_render_paragraph():
    doc = PlainDocument()
    doc.add_paragraph("Testing nineteen four seven")
    expecting = "Testing nineteen four seven\n\n"
    rendered = doc.render()
    rendered = ''.join(rendered)
    assert rendered == expecting

def test_render_amp_paragraph():
    doc = PlainDocument()
    doc.add_paragraph("Cats & Stuff")
    expecting = "Cats & Stuff\n\n"
    rendered = doc.render()
    rendered = ''.join(rendered)
    assert rendered == expecting

def test_render_newline_paragraph():
    doc =  PlainDocument()
    doc.add_paragraph("Cats\n dogs\n wolves")
    expecting = "Cats\n dogs\n wolves\n\n"
    rendered = doc.render()
    rendered = ''.join(rendered)
    assert rendered == expecting

def test_render_codeblock():
    doc = PlainDocument()
    doc.add_codeblock("print(Dogs) {...}")
    expecting = "print(Dogs) {...}\n\n"
    rendered = doc.render()
    rendered = ''.join(rendered)
    assert rendered == expecting
    