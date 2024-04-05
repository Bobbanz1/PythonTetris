from HTMLDocument import HTMLDocument


def test_render_small_heading3():
    doc = HTMLDocument()
    doc.add_heading3("Heading 3")
    expecting = "<h3>Heading 3</h3>"
    assert doc.render() == expecting

def test_render_paragraph():
    doc = HTMLDocument()
    doc.add_paragraph("Testing nineteen four seven")
    expecting = "<p>Testing nineteen four seven</p>"
    assert doc.render() == expecting

def test_escape_html():
    doc = HTMLDocument()
    doc.add_paragraph("Cats <script>run cats.exe</script>")
    expecting = "<p>Cats &lt;script&gt;run cats.exe&lt;/script&gt;</p>"
    assert doc.render() == expecting

def test_render_newline_paragraph():
    doc =  HTMLDocument()
    doc.add_paragraph("Cats\n dogs\n wolves")
    expecting = "<p>Cats<br> dogs<br> wolves</p>"
    assert doc.render() == expecting

def test_render_codeblock():
    doc = HTMLDocument()
    doc.add_codeblock("print(Dogs) {...}")
    expecting = "<pre><code>print(Dogs) {...}</code></pre>"
    assert doc.render() == expecting