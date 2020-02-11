import tkinter as tk
from Functions import onbutton
from Pyscarp import Pyscarp
height = 800
width = 900

root = tk.Tk()


bgcolor='#c4ebf5'
footerColor = '#bad1a5'
Canvas = tk.Canvas(root,height= height, width=width)
Canvas.pack()

#Frames
frameCore = tk.Frame(root, bg=bgcolor)
frameFooter = tk.Frame(root,bg='#bad1a5')
frameHead = tk.Frame(root, bg=footerColor)

frameCore.place(relwidth=1, relheight=1)
frameFooter.place(relwidth=1, relheight=0.3, rely=0.9)
frameHead.place(relwidth=1, relheight=0.1, rely=0)

#Labels
labelCore = tk.Label(frameCore, bg='#bad1a5', text='pass value')
labelCore.place(relwidth=0.45, relheight=0.45, relx=0.2, rely=0.35)

labelPasteUrl = tk.Label(frameHead, bg='#bad1a5', text='Choose page url:')
labelPasteUrl.place(relwidth=0.13, relheight=0.25, relx=0, rely=0.35)

labelPasteFileName = tk.Label(frameHead, bg='#bad1a5', text='File name .txt:')
labelPasteFileName.place(relwidth=0.39, relheight=0.25, relx=0.17, rely=0.35)

#Entries
entryCore = tk.Entry(frameCore, bg='#bad1a5')
entryCore.place(relwidth=0.25, relheight=0.10, relx=0.40, rely=0.2)

entryUrlHead = tk.Entry(frameHead, bg='#c4ebf5')
entryUrlHead.place(relwidth=0.15, relheight=0.25, relx=0.15, rely=0.35)

entryFileNameHead = tk.Entry(frameHead, bg='#c4ebf5')
entryFileNameHead.place(relwidth=0.15, relheight=0.25, relx=0.43, rely=0.35)

#Buttons
button = tk.Button(frameCore,text='Show something', fg='black', font=40, command = lambda: onbutton.click(None, entryCore.get()))
button.place(relwidth=0.15,relheight=0.10, relx=0.2, rely=0.2)

buttonHead = tk.Button(frameHead,text='Create file', fg='black', font=40, command = lambda: Pyscarp().save_all_into_file(entryFileNameHead.get(), entryUrlHead.get()))
buttonHead.place(relwidth=0.15, relheight=0.25, relx=0.59, rely=0.35)

# command = onbutton.click(None, entryCore.get())

#command=lambda: click_function(entryCore.get()))


root.mainloop()
