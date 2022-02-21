import tkinter as tk
from tkinter import ttk


class NoteBook(ttk.Notebook):
    def __init__(self, *args, **kwargs):
        super(NoteBook, self).__init__(args[0])

    