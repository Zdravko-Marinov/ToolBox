from curses import window
import tkinter as tk
import GUI.GUI_WhatWeb as gui_whatweb

gui_TK= tk.Tk()

def start():
    gui_TK.minsize(500,500)
    gui_TK.geometry("1000x500")
    gui_whatweb.drawGUI(gui_TK)
    gui_TK.mainloop()