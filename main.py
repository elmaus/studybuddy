
from re import sub
import tkinter as tk
import sqlite3

from rightframe import RightFrame
from tkinter import LEFT, RAISED, W, ttk
from sheet import Sheet
from content import Folder
from blank import Blank
import db_init as db
from flush.flmain import Flush

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__()

        self.mainbook = ttk.Notebook(self)
        self.mainbook.pack(fill="both", expand=1)

        self.notepad = tk.Frame(self.mainbook, pady=5)
        self.notepad.pack(fill='both', expand=1)
        self.mainbook.add(self.notepad, text="Notes")

        self.flush = Flush(self.mainbook, pady=5)
        self.flush.pack(fill='both', expand=1)
        self.mainbook.add(self.flush, text="Flush")

        self.right_frame = RightFrame(self.notepad, app=self, bd=1, relief=RAISED)
        self.right_frame.grid(row=0, column=0, sticky="nw")

        self.folders = []
        self.open_notes = []

        self.notebook = ttk.Notebook(self.notepad)
        self.notebook.grid(row=0, column=1, sticky="n")

        self.blank = Blank(self.notebook)
        self.blank.pack(fill='both', expand=1)
        self.open_notes.append(self.blank)
        self.notebook.add(self.blank, text="Blank")
        

if __name__ == "__main__":
    app = App()
    # db.create_database()
    # db.create_subject()
    # db.create_flush_table()
    app.mainloop()