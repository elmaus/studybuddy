
import tkinter as tk
from tkinter import ttk
from turtle import width
import db_init as db
from tkinter import  LEFT, RIGHT, scrolledtext, messagebox

class Blank(tk.Frame):
    def __init__(self, *args, **kwargs):
        super(Blank, self).__init__(args[0])

        self.subVar = tk.StringVar()
        self.titleVar = tk.StringVar(self)
        self.categoryVar = tk.StringVar(self)

        self.header = tk.Frame(self,padx=8)
        self.header.pack(fill='x', expand=1)

        self.info_frame = tk.Frame(self.header)
        self.info_frame.pack(side=LEFT)

        self.subject_lbl = tk.Label(self.info_frame, text="Subject:", justify=LEFT, padx=10)
        self.subject_lbl.grid(row=0, column=0)

        self.subbox = ttk.Combobox(self.info_frame, textvariable=self.subVar)
        self.subbox.grid(row=0, column=1, sticky='w')
        self.subbox['value'] = db.get_subjects()
        self.subbox.current()
        self.subbox.bind("<<ComboboxSelected>>", self.display_categories)

        self.category_lbl = tk.Label(self.info_frame, text="Category:", justify=LEFT, padx=10)
        self.category_lbl.grid(row=0, column=2, sticky='w')

        self.catbox = ttk.Combobox(self.info_frame, textvariable=self.categoryVar)
        self.catbox.grid(row=0, column=3, sticky='w')

        self.title_lbl = tk.Label(self.info_frame, text="Title:", justify=LEFT, padx=10)
        self.title_lbl.grid(row=1, column=0, sticky='w')

        self.title_entry = tk.Entry(self.info_frame, textvariable=self.titleVar, width=59)
        self.title_entry.grid(row=1, column=1, sticky='w', columnspan=3)

        self.btn_frame = tk.Frame(self.header)
        self.btn_frame.pack(side=RIGHT, anchor='n')

        self.save_btn = tk.Button(self.btn_frame, width=8, bd=1, text="Save", command=self.save)
        self.save_btn.pack(side=RIGHT, anchor='n')
        
        self.text_box = scrolledtext.ScrolledText(self, width=60, height=25, padx=5, pady=5)
        self.text_box.pack()

    def save(self):
        subject = self.subVar.get()
        category = self.categoryVar.get()
        title = self.titleVar.get()
        content = self.text_box.get("1.0", 'end')

        if subject and category and title and content:

            if not db.get_subject(subject):
                db.create_subject(subject)

            if not db.get_category(category):
                db.create_category(category, subject)

            db.create_note(category, title, content)
            messagebox.showinfo("Successful", f"New notes has been saved as {title}")

        else:
            print(db.get_category(category))
            print("incomplete input")


    def display_categories(self, e):
        self.catbox['value'] = db.get_categories(self.subVar.get())
        if len(self.catbox['value']) > 0:
            self.catbox.current(0)

