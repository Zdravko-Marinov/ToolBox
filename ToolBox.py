#!/bin/python3
import GUI.GUI_Main as gui
import os as os

def guiStart():
    if os.geteuid() !=0: # check if the program is running as root
            exit("You need to have root privileges to run ToolBox")
    else:
        gui.start()

guiStart()