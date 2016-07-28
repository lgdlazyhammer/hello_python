#!my test for python step one

import tkinter

from mymodule import show_sys_path

top = tkinter.Tk()

label = tkinter.Label(top,text=show_sys_path.showpath())

label.pack()

tkinter.mainloop()

