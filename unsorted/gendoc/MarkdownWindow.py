import customtkinter as CTk
from DocGenerator import MarkdownDocument

class MarkdownWindow(CTk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Markdown File Creator")
        self.geometry("500x300")
        self.markdown = MarkdownDocument.MarkdownDocument()
        self.minsize(300, 200)

        # creates a 2x2 grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0,1,3), weight=1)
        
        self.textbox = CTk.CTkTextbox(self, state="disabled")
        self.textbox.grid(row=0, column=0, columnspan=4, padx=20, pady=(20,0), sticky="nsew")


        # Row 1
        ## Headers
        self.button_h1 = CTk.CTkButton(self, text="Add Header 1", command=self.add_header1, corner_radius=0)
        self.button_h1.grid(row=1, column=0, padx=(20,0), pady=(10,0), sticky="nsew")
        self.button_h2 = CTk.CTkButton(self, text="Add Header 2", command=self.add_header2, corner_radius=0)
        self.button_h2.grid(row=1, column=1, pady=(10,0), sticky="nsew")
        self.button_h3 = CTk.CTkButton(self, text="Add Header 3", command=self.add_header3, corner_radius=0)
        self.button_h3.grid(row=1, column=2, pady=(10,0), sticky="nsew")

        # Row 2
        ## Paragraph, Codeblock, Save
        self.button_p = CTk.CTkButton(self, text="Add Paragraph", command=self.add_paragraph, corner_radius=0)
        self.button_p.grid(row=2, column=0, padx=(20,0), sticky="nsew")
        self.button_save = CTk.CTkButton(self, text="Save", command=self.save, corner_radius=0)
        self.button_save.grid(row=2, column=1, sticky="nsew")
        self.button_code = CTk.CTkButton(self, text="Add Codeblock", command=self.add_codeblock, corner_radius=0)
        self.button_code.grid(row=2, column=2, sticky="nsew")

        # Row 3
        ## Delete
        self.button_clear = CTk.CTkButton(self, text="Delete", command=self.clear, corner_radius=0)
        self.button_clear.grid(row=3, column=0, padx=(20,0), pady=(0,10), columnspan=3, sticky="nsew")


    def save(self):
        file = open("markdown_output.md", "w")
        for entries in self.markdown.render():
            file.write(entries + "\n")
        file.close()

    def clear(self):
        if len(self.textbox.get("0.0", "end")) > 0:
            self.textbox.configure(state="normal")
            self.textbox.delete("0.0", "end")
            self.markdown._document_parts.clear()
            self.textbox.configure(state="disabled")

    def add_header1(self):
        self.texter = CTk.CTkInputDialog(text="Type in stuff:", title="Header 1")

        inputted_text = self.texter.get_input()

        if inputted_text == None:
            return
        else:
            self.markdown.add_heading1(inputted_text)
            self.textbox.configure(state="normal")
            if len(self.textbox.get("0.0", "end")) > 0:
                self.textbox.delete("0.0", "end")
            for entry in self.markdown.render():
                self.textbox.insert("insert", entry)
            self.textbox.configure(state="disabled")

    def add_header2(self):
        self.texter = CTk.CTkInputDialog(text="Type in stuff:", title="Header 2")

        inputted_text = self.texter.get_input()

        if inputted_text == None:
            return
        else:
            self.markdown.add_heading2(inputted_text)
            self.textbox.configure(state="normal")
            if len(self.textbox.get("0.0", "end")) > 0:
                self.textbox.delete("0.0", "end")
            for entry in self.markdown.render():
                self.textbox.insert("insert", entry)
            self.textbox.configure(state="disabled")

    def add_header3(self):
        self.texter = CTk.CTkInputDialog(text="Type in stuff:", title="Header 3")

        inputted_text = self.texter.get_input()

        if inputted_text == None:
            return
        else:
            self.markdown.add_heading3(inputted_text)
            self.textbox.configure(state="normal")
            if len(self.textbox.get("0.0", "end")) > 0:
                self.textbox.delete("0.0", "end")
            for entry in self.markdown.render():
                self.textbox.insert("insert", entry)
            self.textbox.configure(state="disabled")

    def add_paragraph(self):
        self.texter = CTk.CTkInputDialog(text="Type in stuff:", title="Paragraph")

        inputted_text = self.texter.get_input()

        if inputted_text == None:
            return
        else:
            self.markdown.add_paragraph(inputted_text)
            self.textbox.configure(state="normal")
            if len(self.textbox.get("0.0", "end")) > 0:
                self.textbox.delete("0.0", "end")
            for entry in self.markdown.render():
                self.textbox.insert("insert", entry)
            self.textbox.configure(state="disabled")

    def add_codeblock(self):
        self.texter = CTk.CTkInputDialog(text="Type in stuff:", title="Codeblock")

        inputted_text = self.texter.get_input()

        if inputted_text == None:
            return
        else:
            self.markdown.add_codeblock(inputted_text)
            self.textbox.configure(state="normal")
            if len(self.textbox.get("0.0", "end")) > 0:
                self.textbox.delete("0.0", "end")
            for entry in self.markdown.render():
                self.textbox.insert("insert", entry)
            self.textbox.configure(state="disabled")
