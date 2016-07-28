#!thi is my first dialog  (start line)

# (document annotation)

# (module import)
from tkinter import (Tk, Label, Button, Menu, Listbox, Entry, RIGHT, LEFT, END)
# (class defination)

# (function defination)
#when button clicked this will be triggered
def clickButton():
    print('input value: ', E1.get())
    

# (main program)
top = Tk()
top.tk.eval('package require Tix')
top.title('Hello World')
top.geometry('400x200') 

def hello():
    print('hello')

menubar = Menu(top)

#创建下拉菜单File，然后将其加入到顶级的菜单栏中
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=top.quit)
menubar.add_cascade(label="File", menu=filemenu)
#显示菜单
top.config(menu=menubar)


#li     = ['C','python','php','html','SQL','java']
#listb  = Listbox(top)          #  创建两个列表组件
#for item in li:                 # 第一个小部件插入数据
 #   listb.insert(0,item)
#listb.pack()                    # 将小部件放置到主窗口中

#lb = Label(top, text = 'Animals in ')
#lb.pack()

E1 = Entry(top, bd =5)

E1.pack(side = RIGHT)


qb = Button(top, text='quit', command=clickButton, bg='red', fg='white')
qb.pack(side=LEFT)

top.mainloop()