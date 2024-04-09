import customtkinter as CTk
from DocGenerator import PlainDocument

class TextWindow(CTk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Text File Creator")
        self.geometry("500x300")
        self.plain = PlainDocument.PlainDocument()
        self.minsize(300, 200)

        # creates a 2x2 grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0,1,3), weight=1)
        
        self.textbox = CTk.CTkTextbox(self, state="disabled")
        self.textbox.grid(row=0, column=0, columnspan=4, padx=20, pady=(20,0), sticky="nsew")


        # Row 1
        ## Text, Delete, Save
        self.button_p = CTk.CTkButton(self, text="Add Text", command=self.add_paragraph, corner_radius=0)
        self.button_p.grid(row=1, column=0, padx=(20,0), pady=(10,10), sticky="nsew")
        self.button_clear = CTk.CTkButton(self, text="Delete", command=self.clear, corner_radius=0)
        self.button_clear.grid(row=1, column=1, pady=(10,10), sticky="nsew")
        self.button_save = CTk.CTkButton(self, text="Save", command=self.save, corner_radius=0)
        self.button_save.grid(row=1, column=2, pady=(10,10), sticky="nsew")

    def save(self):
        file = open("plain_output.txt", "w")
        for entries in self.plain.render():
            file.write(entries)
        file.close()

    def clear(self):
        if len(self.textbox.get("0.0", "end")) > 0:
            self.textbox.configure(state="normal")
            self.textbox.delete("0.0", "end")
            self.plain._document_parts.clear()
            self.textbox.configure(state="disabled")

    def add_paragraph(self):
        self.texter = CTk.CTkInputDialog(text="Type in stuff:", title="Paragraph")

        inputted_text = self.texter.get_input()

        if inputted_text == None:
            return
        else:
            self.plain.add_paragraph(inputted_text)
            self.textbox.configure(state="normal")
            if len(self.textbox.get("0.0", "end")) > 0:
                self.textbox.delete("0.0", "end")
            for entry in self.plain.render():
                self.textbox.insert("insert", entry)
            self.textbox.configure(state="disabled")
