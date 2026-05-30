import tkinter as tk

class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master
        self.current_screen = None

        # Placeholder label until screens are implemented
        placeholder = tk.Label(self, text="GUI Loaded Successfully!", font=("Arial", 24))
        placeholder.pack(pady=50)

    def show_screen(self, screen_class):
        """Destroys current screen and loads a new one."""
        if self.current_screen is not None:
            self.current_screen.destroy()

        self.current_screen = screen_class(self)
        self.current_screen.pack(fill="both", expand=True)