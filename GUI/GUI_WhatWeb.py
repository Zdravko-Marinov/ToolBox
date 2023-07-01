import tkinter as tk
import Modules.whatweb.WhatWebModule as whatweb

class Vars:
    def __init__(self):
        self.is_stealthVar = None
        self.is_agressiveVar = None
        self.is_heavyVar = None
        self.targetVar = None
        self.root = None

        
Vars_ = Vars()

def empty_space(_root,_column,_row):
    tk.Label(_root,text=" ").grid(column=_column,row=_row)

#Function that will pass all the values from fields and execute command
def enterValue():
    whatweb.target = Vars_.targetVar.get() # set the target we have typed out 
    whatweb.masterRoot = Vars_.root
    whatweb.command_builder() # build the command and execute

#Function for switching on and off the options
def swtichBool():
    whatweb.is_stealth = Vars_.is_stealthVar.get()
    whatweb.is_aggressive = Vars_.is_agressiveVar.get()
    whatweb.is_heavy = Vars_.is_heavyVar.get()


#Funtion that will use the variables to set up the tk vars
def initValues():
    Vars_.is_stealthVar = tk.BooleanVar()

    Vars_.is_agressiveVar = tk.BooleanVar()

    Vars_.is_heavyVar = tk.BooleanVar()

    Vars_.targetVar = tk.StringVar()

#Function that will be called from Main GUI to draw all the elements
def drawGUI(root):

    initValues()
    Vars_.root = root

    tk.Label(root,text="WhatWeb").grid(column=1,row=0)

    empty_space(root,0,1)
    empty_space(root,0,2)

    tk.Label(root,text="Enter Target URL/IP ->").grid(column=0,row=3)
    tk.Entry(root,textvariable=Vars_.targetVar).grid(column=1,row=3)
    tk.Button(root,text="EXECUTE",command=enterValue).grid(column=4,row=3)

    empty_space(root,0,4)
    empty_space(root,0,5)

    tk.Label(root,text="Scan Mode (Optional)").grid(column=1,row=5)
    tk.Checkbutton(root,text= "Stealth",command=swtichBool,variable=Vars_.is_stealthVar).grid(column=0,row=6)
    tk.Checkbutton(root,text= "Agressive",command=swtichBool,variable=Vars_.is_agressiveVar).grid(column=1,row=6)
    tk.Checkbutton(root,text= "Heavy",command=swtichBool,variable=Vars_.is_heavyVar).grid(column=2,row=6)