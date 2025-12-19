# app/main.py
import tkinter as tk
from .ui import AppUI
from .controller import Controller

def main():
    root = tk.Tk()
    ui = AppUI(root)
    Controller(root, ui)
    root.mainloop()

if __name__ == "__main__":
    main()
