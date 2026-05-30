import tkinter as tk
from main_window import MainWindow

def main():
    root = tk.Tk()
    root.title("Guess The Word — GUI Version")
    root.geometry("800x600")  # You can adjust this later

    app = MainWindow(root)
    app.pack(fill="both", expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()