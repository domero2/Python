from tkinter import *

root = Tk()
#thLable = Label(root, text="This is to easy")
#thLable.pack()
''
topFrame = Frame(root)
topFrame.pack()
bottomFram = Frame(root)
bottomFram.pack(side=BOTTOM)

Firstbutton = Button(topFrame, text="FirstButton",fg="red")
Secondbutton = Button(topFrame, text="SecondButton",fg="blue")
Thirdbutton = Button(topFrame, text="ThirdButton",fg="green")
Fourbutton = Button(topFrame, text="ThirdButton",fg="yellow")

Firstbutton.pack(side=LEFT)
Secondbutton.pack(side=LEFT)
Thirdbutton.pack(side=LEFT)
Fourbutton.pack(side=BOTTOM)

root.mainloop()