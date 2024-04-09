import customtkinter as CTk
import HTMLWindow as HTW
import MarkdownWindow as MDW
import TextWindow as TW

CTk.set_appearance_mode("Dark")
CTk.set_default_color_theme("blue")

class App(CTk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configure Window
        self.title("Document Creator")
        self.geometry(f"{500}x{400}")

        self.label = CTk.CTkLabel(self, text="Document Creator v1.0", font=CTk.CTkFont(size=20, weight="bold"))
        self.label.pack(side="top", padx=20, pady=20)

        # Window for HTML File Creator Version
        self.button_html = CTk.CTkButton(self, text="HTML Document", command=self.open_html_window, font=CTk.CTkFont(weight="bold"))
        self.button_html.pack(side="top", padx=20, pady=20)

        # Window for Markdown File Creator Version
        self.button_md = CTk.CTkButton(self, text="Markdown Document", command=self.open_markdown_window, font=CTk.CTkFont(weight="bold"))
        self.button_md.pack(side="top", padx=20, pady=20)

        # Window for Text File Creator Version
        self.button_txt = CTk.CTkButton(self, text="Plain Document", command=self.open_plain_window, font=CTk.CTkFont(weight="bold"))
        self.button_txt.pack(side="top", padx=20, pady=20)
        self.toplevel_window = None

    def open_html_window(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = HTW.HTMLWindow(self)
        else:
            self.toplevel_window.focus()

    def open_markdown_window(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = MDW.MarkdownWindow(self)
        else:
            self.toplevel_window.focus()

    def open_plain_window(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = TW.TextWindow(self)
        else:
            self.toplevel_window.focus()

if __name__ == "__main__":
    app = App()
    app.mainloop()
    