from sqlite3 import Row
import tkinter as tk
import weakref
import Modules.whatweb.WhatWebModule as whatweb

def empty_space(_root,_column,_row):
    tk.Label(_root,text=" ").grid(column=_column,row=_row)

def enterValue():
    whatweb.target = targetVar.get()
    print(whatweb.target)

def swtichBool():
    whatweb.is_stealth = is_stealthVar.get()
    whatweb.is_aggressive = is_agressiveVar.get()
    whatweb.is_heavy = is_heavyVar.get()

def initValues():
    global is_stealthVar
    is_stealthVar = tk.BooleanVar()

    global is_agressiveVar
    is_agressiveVar = tk.BooleanVar()

    global is_heavyVar
    is_heavyVar = tk.BooleanVar()

    global targetVar
    targetVar = tk.StringVar()

def drawButtons(root):
    initValues()
    tk.Label(root,text="WhatWeb").grid(column=1,row=0)

    empty_space(root,0,1)
    empty_space(root,0,2)

    tk.Label(root,text="Enter Target URL/IP ->").grid(column=0,row=3)
    tk.Entry(root,textvariable=targetVar).grid(column=1,row=3)

    empty_space(root,0,4)
    empty_space(root,0,5)

    tk.Label(root,text="Scan Mode (Optional)").grid(column=1,row=5)
    tk.Checkbutton(root,text= "Stealth",command=swtichBool,variable=is_stealthVar).grid(column=0,row=6)
    tk.Checkbutton(root,text= "Agressive",command=swtichBool,variable=is_agressiveVar).grid(column=1,row=6)
    tk.Checkbutton(root,text= "Heavy",command=swtichBool,variable=is_heavyVar).grid(column=2,row=6)
    