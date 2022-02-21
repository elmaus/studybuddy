import tkinter as tk
from turtle import width
from sheet import Sheet

class Note(tk.Frame):
    def __init__(self, *args, **kwargs):
        super(Note, self).__init__(args[0])

        self.app = kwargs['app']
        self.tab = tk.Label(self, text="", width=3)
        self.tab.grid(row=0, column=0, sticky='w')
        self.id = kwargs['id']
        self.category = kwargs['category']
        self.title = kwargs['title']
        self.content = kwargs['content']

        self.label = tk.Label(self, text=kwargs['title'], justify=tk.LEFT, anchor='w')
        self.label.grid(row=0, column=1, sticky='w')

        self.label.bind("<Button-1>", self.open_note)

    
    def open_note(self, e):
        sheet1 = Sheet(self.app.notebook, app=self.app, id=self.id, title=self.title, content=self.content)
        sheet1.pack(fill='both', expand=1)
        self.app.open_notes.append(sheet1)

        self.app.notebook.add(sheet1, text=self.title[:8])

        sheet1.title_entry.insert(0, self.title)
        sheet1.title_entry.config(state='disabled')

        sheet1.text_box.insert('end', self.content)
        sheet1.text_box.config(state="disabled")
        sheet1.focus()

        

class Folder(tk.Frame):
    def __init__(self, *args, **kwargs):
        super(Folder, self).__init__(args[0])
        self.open = False
        self.app = kwargs['app']
        self.master = kwargs['master']
        self.child = kwargs['child']
        self.notes = []

        self.label = tk.Label(self, text=kwargs["category"], bd=1, pady=5, padx=8, relief=tk.RAISED, width=26, justify=tk.LEFT, anchor='w')
        self.label.pack(anchor="nw")
        self.label.bind("<Button-1>", self.dropdown)

        

        # for c in self.notes:
        #     new = Note(self.container, note=c)
        #     self.notes.append(new)
        #     new.pack()


    def enter(self, instance):
        pass

    def dropdown(self, instance):
        if not self.open:
            self.container = tk.Frame(self, bd=1, relief=tk.SUNKEN)
            self.container.pack(expand=1, fill="both")
            for c in self.child:
                new = Note(self.container, id=c[0], title=c[1], content=c[2], category=c[3], app=self.app)
                self.notes.append(new)
                new.pack(anchor='w')
                self.app.update_idletasks()
            self.open = True
        else:
            self.container.destroy()
            self.app.update_idletasks()
            self.open = False

        self.master.scrollview.reupdate()
        