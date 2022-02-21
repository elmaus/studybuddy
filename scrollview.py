
import tkinter as tk
from tkinter import RAISED, LEFT, BOTH, SUNKEN, VERTICAL, RIGHT


class ScrollView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, args[0], bd=1, relief=SUNKEN)

        self.WIDTH = kwargs['width']
        self.HEIGHT = kwargs['height']
        
        self.canvas = tk.Canvas(self, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)

        if kwargs['scroll']:
            self.scrollbar = tk.Scrollbar(self, orient=VERTICAL, command=self.canvas.yview)
            self.scrollbar.pack(side=RIGHT, fill='y')

            self.canvas.configure(yscrollcommand=self.scrollbar.set)
            self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.container = tk.Frame(self.canvas)
        self.canvas.create_window((0,0), window=self.container, anchor='nw')

    def reupdate(self):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
