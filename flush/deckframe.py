import tkinter as tk
from tkinter import ttk
from scrollview import ScrollView
import db_init as db
from flush.deck import Deck



class DeckFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        super(DeckFrame, self).__init__(args[0], padx=5)

        # self.app = kwargs['app']
        self.subjects = db.get_subjects()
        self.subVar = tk.StringVar()

        self.folders = []
        self.search_frame = tk.Frame(self)
        self.search_frame.grid(row=0, column=0)

        self.subject_lbl = tk.Label(self.search_frame, text="Deck", justify=tk.LEFT, padx=10)
        self.subject_lbl.grid(row=0, column=0, sticky='w')

        self.catbox = ttk.Combobox(self.search_frame, textvariable=self.subVar, width=22)
        self.catbox.grid(row=0, column=1)
        self.catbox['value'] = db.get_subjects()
        self.catbox.current()
        self.catbox.bind("<<ComboboxSelected>>", self.display_decks)
        self.catbox.bind("<Return>", self.display_decks)

        self.scrollview = ScrollView(self, width=196, height=500, scroll=True)
        self.scrollview.grid(row=1, column=0)

    def display_decks(self, e):
        decks = db.get_all_decks(e.widget.get())
        if len(self.folders) > 0:
            for f in self.folders:
                f.destroy()
        
        for i in range(len(decks)):
            cards = db.get_cards(decks[i])
            new = Deck(self.scrollview.container, master=self, category=decks[i], child=cards)
            new.grid(row=i, column=0,  sticky='w')
            self.folders.append(new)
            self.scrollview.reupdate()
