
import tkinter as tk
from tkinter import ttk
from db_init import get_all_decks, get_deck_categories
from flush.deckframe import DeckFrame
from flush.new_flush import NewFlush
from flush.deck import Deck

class Flush(tk.Frame):
    def __init__(self, *args, **kwargs):
        super(Flush, self).__init__()

        self.app = args[0]
        self.deckframe = DeckFrame(self)
        self.deckframe.grid(row=0, column=0)

        self.deck_categories = get_deck_categories()
    
        self.flush_book = ttk.Notebook(self)
        self.flush_book.grid(row=0, column=1, sticky="nw")

        self.newFlush = NewFlush(self.flush_book)
        self.newFlush.pack(fill='both', expand=1)

        self.flush_book.add(self.newFlush, text="New Card")

        self.decks = ['english', 'math']

        for i in self.decks:
            new = Deck(self.deckframe.scrollview.container, name=i, cards=[])
            new.pack()