from os import stat
import tkinter as tk
from tkinter import Frame, scrolledtext
from tkinter import filedialog
from datetime import datetime

def export_file(toolName,target, output_str):
    path = filedialog.askdirectory()
    timeNow = datetime.now()
    
    reportFile = open(path + "/" + toolName + " " + target + " " + str(timeNow),"w+")
    reportFile.write(output_str)
    reportFile.close

def create_window(root,tool_name,target,output):
    newWindow = tk.Toplevel(root)

    newWindow.title(tool_name + "---->" + target)

    newWindow.minsize(600,500)
    newWindow.geometry("800x500")

    main_frame = tk.Frame(newWindow)
    main_frame.pack(fill=tk.BOTH,expand=1)

    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=tk.LEFT,fill=tk.BOTH,expand=1)

    my_scrollbar = tk.Scrollbar(main_frame,orient=tk.VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind("<Configure>",lambda e: my_canvas.config(scrollregion= my_canvas.bbox("all"))) 

    element_holder = Frame(my_canvas) # Use to hold the leements

    my_canvas.create_window((0,0),window=element_holder,anchor="nw")

    tk.Label(element_holder,text= "Output log").grid(column=0,row=0)
    text_box = tk.Text(element_holder,state='normal',width=80,height=30)
    text_box.grid(column=0,row=1)
    text_box.insert(tk.INSERT,output)
    text_box.configure(state="disabled")

    tk.Button(element_holder,text="Export File",command= lambda: export_file(tool_name,target,output)).grid(column=1,row=1)
