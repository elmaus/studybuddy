import tkinter as tk

class Deck(tk.Frame):
    def __init__(self, *args, **kwargs):
        super(Deck, self).__init__(args[0])
        
        self.deck_name = kwargs['name']
        self.cards = kwargs['cards']

        self.deck_lbl = tk.Label(self, text=self.deck_name)
        self.deck_lbl.pack()