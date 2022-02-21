import tkinter as tk
from tkinter import LEFT, scrolledtext, ttk, messagebox
from db_init import get_all_decks, get_deck_categories, get_deck_category, create_deck_category, create_deck, get_deck, create_card

class NewFlush(tk.Frame):
    def __init__(self, *args, **kwargs):
        super(NewFlush, self).__init__(args[0])

        self.deck_cat_Var = tk.StringVar()
        self.deckVar = tk.StringVar()

        self.deck_frame = tk.Frame(self)
        self.deck_frame.grid(row=0, column=0, sticky='nw')

        self.deck_cat_label = tk.Label(self.deck_frame, text="Category")
        self.deck_cat_label.grid(row=0, column=0)

        self.deck_cat_entry = ttk.Combobox(self.deck_frame, textvariable=self.deck_cat_Var)
        self.deck_cat_entry.grid(row=0, column=1, pady=10)
        self.deck_cat_entry["value"] = get_deck_categories()
        if len(self.deck_cat_entry['value']) > 0:
            self.deck_cat_entry.current(0)
        self.deck_cat_entry.bind("<<ComboboxSelected>>", self.get_decks)
        

        self.deck_label = tk.Label(self.deck_frame, text="Deck Name")
        self.deck_label.grid(row=0, column=2)

        self.deck_entry = ttk.Combobox(self.deck_frame, textvariable=self.deckVar)
        self.deck_entry.grid(row=0, column=3, pady=10)
        if len(self.deck_entry['value']) > 0:
            self.deck_entry.current(0)

        self.side_a_lbl = tk.Label(self, text="Side a: ", justify=LEFT)
        self.side_a_lbl.grid(row=1, column=0, sticky='nw')
        self.side_a = scrolledtext.ScrolledText(self, width=60, height=10, padx=5, pady=5)
        self.side_a.grid(row=2, column=0)


        self.side_b_lbl = tk.Label(self, text="Side b: ", justify=LEFT)
        self.side_b_lbl.grid(row=3, column=0, sticky='nw')
        self.side_b = scrolledtext.ScrolledText(self, width=60, height=10, padx=5, pady=5)
        self.side_b.grid(row=4, column=0)

        self.add_btn = tk.Button(self, text="Add New Card", command=self.add_deck)
        self.add_btn.grid(row=5, column=0, sticky="ne", pady=20, padx=10)


    def get_decks(self):
        self.deck_entry['value'] = get_all_decks(self.deck_cat_Var.get())
        if len(self.deck_entry['value']) > 0:
            self.deck_entry.current(0)

    def add_deck(self):
        category = self.deck_cat_Var.get()
        deck = self.deckVar.get()
        side_a = self.side_a.get("1.0", 'end')
        side_b = self.side_b.get("1.0", 'end')

        try:
            if not get_deck_category(category):
                create_deck_category(category)
            if not get_deck(deck):
                create_deck(deck, category)

            create_card(side_a, side_b, 1, deck)
            messagebox.showinfo("Successful", 'New card has been created')
        except:
            messagebox.showwarning("Failed", "Incomplete input")