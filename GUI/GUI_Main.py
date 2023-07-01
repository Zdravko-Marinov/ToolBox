import tkinter as tk
from tkinter import Frame, scrolledtext
import GUI.GUI_WhatWeb as gui_whatweb

gui_TK= tk.Tk()

main_frame = tk.Frame(gui_TK)
main_frame.pack(fill=tk.BOTH,expand=1)

my_canvas = tk.Canvas(main_frame)
my_canvas.pack(side=tk.LEFT,fill=tk.BOTH,expand=1)

my_scrollbar = tk.Scrollbar(main_frame,orient=tk.VERTICAL,command=my_canvas.yview)
my_scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind("<Configure>",lambda e: my_canvas.config(scrollregion= my_canvas.bbox("all"))) 

element_holder = Frame(my_canvas)

my_canvas.create_window((0,0),window=element_holder,anchor="nw")

def start():
    gui_TK.title("ToolBox")
    gui_TK.minsize(500,500)
    gui_TK.geometry("1000x500")
    gui_whatweb.drawGUI(element_holder)
    gui_TK.mainloop()