from curses import window
import tkinter as tk
import Modules.Modules.nmap.NmapModule as nmap
import Modules.Modules.whatweb.WhatWebModule as whatWeb

guiT= tk.Tk()

def start():
    guiT.minsize(500,500)
    guiT.geometry("1000x500")
    guiT.mainloop()