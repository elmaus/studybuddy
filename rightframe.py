import tkinter as tk
from tkinter import ttk
from scrollview import ScrollView
import db_init as db
from content import Folder


class RightFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        super(RightFrame, self).__init__(args[0], padx=5)

        self.app = kwargs['app']
        self.subjects = db.get_subjects()
        self.subVar = tk.StringVar()

        self.folders = []
        self.search_frame = tk.Frame(self)
        self.search_frame.grid(row=0, column=0)

        self.subject_lbl = tk.Label(self.search_frame, text="Subject", justify=tk.LEFT, padx=10)
        self.subject_lbl.grid(row=0, column=0, sticky='w')

        self.subbox = ttk.Combobox(self.search_frame, textvariable=self.subVar, width=22)
        self.subbox.grid(row=0, column=1)
        self.subbox['value'] = db.get_subjects()
        self.subbox.current()
        self.subbox.bind("<<ComboboxSelected>>", self.display_categories)
        self.subbox.bind("<Return>", self.display_categories)

        self.scrollview = ScrollView(self, width=196, height=500, scroll=True)
        self.scrollview.grid(row=1, column=0)

    def display_categories(self, e):
        categories = db.get_categories(e.widget.get())
        if len(self.folders) > 0:
            for f in self.folders:
                f.destroy()
        
        for i in range(len(categories)):
            notes = db.get_notes(categories[i])
            new = Folder(self.scrollview.container, master=self, app=self.app, category=categories[i], child=notes)
            new.grid(row=i, column=0,  sticky='w')
            self.folders.append(new)
            self.scrollview.reupdate()
