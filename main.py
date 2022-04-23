"""
Music player
only support Windows Platform
"""

import pygame as pg
import tkinter as tk
import help
from tkinter import ttk,messagebox,filedialog
pg.init()
pg.mixer.init()

class ask:
    def __init__(self):
        #ask
        aa = messagebox.askyesno("INFO","Are you sure that you want to quit?")
        print(aa)
        if aa:
            if aa is True:

                root.destroy()
            elif aa is False:
                pass
def find():
    global fn
    fn = filedialog.askopenfilename(title = "Open...",
                                    filetypes=[("mp3", "*.mp3"), ("wave", "*.wav")])
    print(fn)
    pg.mixer.music.load(fn)
    nowp.delete(1.0, tk.END)
    nowp.insert(tk.INSERT, fn)
def play():
    pg.mixer.music.play()
def stop():
    pg.mixer.music.stop()

def pause():
    pg.mixer.music.pause()
def _continue():
    pg.mixer.music.unpause()


def check():
    c = pg.mixer.music.get_busy()
    if c == 0:
         messagebox.showinfo("INFO","IDLE")
    else:
         messagebox.showinfo("INFO","BUSY")
def getname():
        pass


root = tk.Tk()
root.geometry("600x400")
root.resizable(0,0)
root.title("Music Player")
root.protocol("WM_DELETE_WINDOW", ask)
title_frame = tk.Frame(root,
                       height=75,
                       width=600,
                       bg="lightyellow")
hello_Label = tk.Label(title_frame,
                       text="Music Player",
                       font=("Consolas",35),
                       fg="magenta")
hello_Label.pack()
title_frame.pack()
toolbarFrame = tk.LabelFrame(root,
                             height=325,
                             width=150,
                             bg="lightgreen",
                             text="Tool Box")
Choose = ttk.Button(toolbarFrame,
                    text="Open...",
                    width=25,
                    command=find)
Choose.pack()
Start = ttk.Button(toolbarFrame,
                   text="play...",
                   width=25,
                   command=play)
Start.pack()
Continue = ttk.Button(toolbarFrame,
                      text="Continue...",
                      width=25,
                      command=_continue)
Continue.pack()
Pause = ttk.Button(toolbarFrame,
                   text = "Pause...",
                   width = 25,
                   command = pause)
Pause.pack()
Stop = ttk.Button(toolbarFrame,
                  text = "Stop!!!",
                  width = 25,
                  command = stop)
Stop.pack()
check_ = ttk.Button(toolbarFrame,
                    text = "Check!!!",
                    width = 25,
                    command = check)
check_.pack()
HELP = ttk.Button(toolbarFrame,
                  text = "help",
                  width =25,
                  command = help.help)
HELP.pack()
Empty = tk.Frame(toolbarFrame,
                 width = 150,
                 height = 200,
                 bg = "lightgreen")
Empty.pack()
toolbarFrame.pack(side = tk.LEFT)
MainFrame = tk.LabelFrame(root,
                          height = 325,
                          width = 450,
                          bg = "lightgrey",
                          text = "Main")
nowpframe = tk.Frame(MainFrame,
                     width = 450,
                     height = 35)
nowpinfo = tk.Label(nowpframe,
                    text = "Now playing...",
                    font = ("consolas",20),
                    fg = "green")
nowpinfo.pack()
scroll = tk.Scrollbar(nowpframe)
scroll.pack(side = tk.RIGHT,
            fill = tk.Y)
nowp = tk.Text(nowpframe,
               font = ("consolas",15),
               width = 70,
               height = 5)
scroll.config(command = nowp.yview)
nowp.config(yscrollcommand = scroll.set)
nowp.pack()
nowpframe.pack()
voidFrame = tk.Frame(MainFrame,
                     height = 200,
                     width = 450,
                     bg = "lightgrey")
voidFrame.pack()
MainFrame.pack(side = tk.RIGHT)
root.mainloop()


