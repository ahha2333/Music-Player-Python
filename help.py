"""
Help
"""

import tkinter as tk
from tkinter import ttk, messagebox
import os

class help:
    def __init__(self):
        help_d = open("./docs/help.txt","r")
        help_docs = help_d.read()
        help_d.close()
        self.help_screen = tk.Tk()
        self.help_screen.geometry("600x400")
        self.help_screen.resizable(0,0)
        self.help_screen.title("HELP DOCUMENTS")
        MainFrame = tk.LabelFrame(self.help_screen,
                                  height=400,
                                  width=600,
                                  bg="lightgrey",
                                  text="HELP DOCUMENTS")
        helpframe = tk.Frame(MainFrame,
                             width=450,
                             height=400)
        helpinfo = tk.Label(helpframe,
                            text="HELP DOCUMENTS...",
                            font=("consolas", 20),
                            fg="green")
        helpinfo.pack()
        scroll = tk.Scrollbar(helpframe)
        scroll.pack(side=tk.RIGHT,
                    fill=tk.Y)
        help__ = tk.Text(helpframe,
                       font=("consolas", 15),
                       width=70,
                       height=500)
        scroll.config(command=help__.yview)
        help__.config(yscrollcommand=scroll.set)
        help__.pack()
        help__.delete(1.0, tk.END)
        help__.insert(tk.INSERT, help_docs)
        helpframe.pack()
        voidFrame = tk.Frame(MainFrame,
                             height=2000,
                             width=450,
                             bg="lightgrey")
        voidFrame.pack()
        MainFrame.pack(side=tk.RIGHT)
        self.help_screen.mainloop()




