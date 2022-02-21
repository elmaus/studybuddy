
import tkinter as tk
from tkinter import  LEFT, RIGHT, scrolledtext
from turtle import width
import db_init as db

class Sheet(tk.Frame):
    def __init__(self, *args, **kwargs):
        super(Sheet, self).__init__(args[0])

        self.app = kwargs['app']

        self.id = kwargs['id']
        self.orig_title = kwargs['title']
        self.orig_content = kwargs['content']

        self.titleVar = tk.StringVar(self)
        self.categoryVar = tk.StringVar(self)

        self.header = tk.Frame(self,padx=8)
        self.header.pack(fill='x', expand=1)

        self.info_frame = tk.Frame(self.header)
        self.info_frame.pack(side=LEFT)

        self.title_lbl = tk.Label(self.info_frame, text="Title:", justif=LEFT)
        self.title_lbl.grid(row=0, column=0, sticky='w')

        self.title_entry = tk.Entry(self.info_frame, textvariable=self.titleVar, width=28)
        self.title_entry.bind('<KeyPress>', self.active_save)
        self.title_entry.grid(row=0, column=1, sticky='w')

        # self.category_lbl = tk.Label(self.info_frame, text="Category:", justify=LEFT)
        # self.category_lbl.grid(row=1, column=0, sticky="w")

        # self.category_entry = tk.Entry(self.info_frame, textvariable=self.categoryVar, width=28)
        # self.category_entry.grid(row=1, column=1, sticky="w")

        self.btn_frame = tk.Frame(self.header)
        self.btn_frame.pack(side=RIGHT, anchor='n')

        self.close_btn = tk.Button(self.btn_frame, width=8, bd=1, text="Close", command=self.close_note)
        self.close_btn.pack(side=RIGHT, anchor='n')

        
        self.save_btn = tk.Button(self.btn_frame, width=8, bd=1, text="Save", command=self.save)
        self.save_btn.pack(side=RIGHT, anchor='n')
        self.save_btn.config(state="disabled")
        
        self.edit_btn = tk.Button(self.btn_frame, width=8, bd=1, text="Edit", command=self.edit)
        self.edit_btn.pack(side=RIGHT, anchor='n')

        self.delete_btn = tk.Button(self.btn_frame, width=8, bd=1, text="Delete", command=self.delete_note)
        self.delete_btn.pack(side=RIGHT, anchor='n')

        self.text_box = scrolledtext.ScrolledText(self, width=60, height=25, padx=5, pady=5)
        self.text_box.pack()
        self.text_box.bind('<KeyPress>', self.active_save)

    def active_save(self, e):
        if self.text_box['state'] == "normal":
            self.save_btn.config(state='normal')

    def save(self):
        title = self.titleVar.get()
        content = self.text_box.get('1.0', 'end')
        
        db.update_note(self.id, title, content)
        
        self.text_box.config(state='disabled')
        self.save_btn.config(state="disabled")
        self.title_entry.config(state="disabled")

    def update_scroll(self, e):
        self.scrollview.reupdate()

    def edit(self):
        self.text_box.config(state="normal")
        self.title_entry.config(state="normal")
        self.text_box.focus()

    def delete_note(self):
        pass

    def close_note(self):
        self.destroy()