import customtkinter
from HTMLWindow import HTMLWindow

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # configure window
        self.title("Attempt Window")
        self.geometry(f"{500}x{400}")

        self.button_html = customtkinter.CTkButton(self, text="HTML Document", command=self.open_html_window)
        self.button_html.pack(side="top", padx=20, pady=20)
        self.toplevel_window = None

    def open_html_window(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = HTMLWindow(self)
        else:
            self.toplevel_window.focus()

if __name__ == "__main__":
    app = App()
    app.mainloop()