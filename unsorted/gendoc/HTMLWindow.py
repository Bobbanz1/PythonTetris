import customtkinter
from HTMLDocument import HTMLDocument

class HTMLWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("HTML Window")
        self.geometry("500x300")
        self.html = HTMLDocument()
        self.minsize(300, 200)

        # creates a 2x2 grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0,1,3), weight=1)
        
        self.textbox = customtkinter.CTkTextbox(self, state="disabled")
        self.textbox.grid(row=0, column=0, columnspan=4, padx=20, pady=(20,0), sticky="nsew")


        # Row 1
        self.button_h1 = customtkinter.CTkButton(self, text="Add Header 1", command=self.add_header1, corner_radius=0)
        self.button_h1.grid(row=1, column=0, padx=(20,0), pady=(10,0), sticky="nsew")
        self.button_h2 = customtkinter.CTkButton(self, text="Add Header 2", command=self.add_header2, corner_radius=0)
        self.button_h2.grid(row=1, column=1, pady=(10,0), sticky="nsew")
        self.button_h3 = customtkinter.CTkButton(self, text="Add Header 3", command=self.add_header3, corner_radius=0)
        self.button_h3.grid(row=1, column=2, pady=(10,0), sticky="nsew")

        # Row 2
        self.button_p = customtkinter.CTkButton(self, text="Add Paragraph", command=self.add_paragraph, corner_radius=0)
        self.button_p.grid(row=2, column=0, padx=(20,0), pady=(0,10), sticky="nsew")
        self.button_save = customtkinter.CTkButton(self, text="Save", command=self.save, corner_radius=0)
        self.button_save.grid(row=2, column=1, pady=(0,10), sticky="nsew")
        self.button_code = customtkinter.CTkButton(self, text="Add Codeblock", command=self.add_codeblock, corner_radius=0)
        self.button_code.grid(row=2, column=2, pady=(0,10), sticky="nsew")

    def save(self):
        file = open("output.txt", "w")
        for entries in self.html.render():
            file.write(entries + "\n")
        file.close()

    def add_header1(self):
        self.texter = customtkinter.CTkInputDialog(text="Type in stuff:", title="Header 1")

        self.html.add_heading1(self.texter.get_input())
        self.textbox.configure(state="normal")
        if len(self.textbox.get("0.0", "end")) > 0:
            self.textbox.delete("0.0", "end")
        for entry in self.html.render():
            self.textbox.insert("insert", entry + "\n")
        self.textbox.configure(state="disabled")

    def add_header2(self):
        self.texter = customtkinter.CTkInputDialog(text="Type in stuff:", title="Header 2")

        self.html.add_heading2(self.texter.get_input())
        self.textbox.configure(state="normal")
        if len(self.textbox.get("0.0", "end")) > 0:
            self.textbox.delete("0.0", "end")
        for entry in self.html.render():
            self.textbox.insert("insert", entry + "\n")
        self.textbox.configure(state="disabled")

    def add_header3(self):
        self.texter = customtkinter.CTkInputDialog(text="Type in stuff:", title="Header 3")

        self.html.add_heading3(self.texter.get_input())
        self.textbox.configure(state="normal")
        if len(self.textbox.get("0.0", "end")) > 0:
            self.textbox.delete("0.0", "end")
        for entry in self.html.render():
            self.textbox.insert("insert", entry + "\n")
        self.textbox.configure(state="disabled")

    def add_paragraph(self):
        self.texter = customtkinter.CTkInputDialog(text="Type in stuff:", title="Paragraph")

        self.html.add_paragraph(self.texter.get_input())
        self.textbox.configure(state="normal")
        if len(self.textbox.get("0.0", "end")) > 0:
            self.textbox.delete("0.0", "end")
        for entry in self.html.render():
            self.textbox.insert("insert", entry + "\n")
        self.textbox.configure(state="disabled")

    def add_codeblock(self):
        self.texter = customtkinter.CTkInputDialog(text="Type in stuff:", title="Codeblock")

        self.html.add_codeblock(self.texter.get_input())
        self.textbox.configure(state="normal")
        if len(self.textbox.get("0.0", "end")) > 0:
            self.textbox.delete("0.0", "end")
        for entry in self.html.render():
            self.textbox.insert("insert", entry + "\n")
        self.textbox.configure(state="disabled")

