import tkinter as tk
from tkinter import *

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

CanvaCore = tk.Canvas(frameCore, bg='black')
CanvaCore.place(relwidth=0.75, relheight=0.45, relx=0.2, rely=0.35)
#Labels
labelCore = tk.Label(frameCore, text='test')
labelCore.place(relwidth=0.75, relheight=0.45, relx=0.2, rely=0.35)

labelPasteUrl = tk.Label(frameHead, bg='#bad1a5', text='Choose page url:')
labelPasteUrl.place(relwidth=0.13, relheight=0.25, relx=0, rely=0.35)

labelPasteFileName = tk.Label(frameHead, bg='#bad1a5', text='File name .txt:')
labelPasteFileName.place(relwidth=0.39, relheight=0.25, relx=0.17, rely=0.35)

#Entries
entryCoreFileName = tk.Entry(frameCore, bg='#bad1a5')
entryCoreFileName.place(relwidth=0.25, relheight=0.10, relx=0.40, rely=0.2)

entryCoreText = tk.Entry(frameCore, bg='#bad1a5')
entryCoreText.place(relwidth=0.25, relheight=0.10, relx=0.70, rely=0.2)

entryUrlHead = tk.Entry(frameHead, bg='#c4ebf5')
entryUrlHead.place(relwidth=0.15, relheight=0.25, relx=0.15, rely=0.35)

entryFileNameHead = tk.Entry(frameHead, bg='#c4ebf5')
entryFileNameHead.place(relwidth=0.15, relheight=0.25, relx=0.43, rely=0.35)

#Buttons
button = tk.Button(frameCore,text='Show something', fg='black', font=40,
                   command = lambda: onbutton().searching_results(Pyscarp().search_word_from_file(entryCoreText.get(),entryCoreFileName.get()),labelCore))
button.place(relwidth=0.15,relheight=0.10, relx=0.2, rely=0.2)

buttonHead = tk.Button(frameHead,text='Create file', fg='black', font=40, command = lambda: Pyscarp().save_all_into_file(entryFileNameHead.get(), entryUrlHead.get()))
buttonHead.place(relwidth=0.15, relheight=0.25, relx=0.59, rely=0.35)

# scrollbar = tk.Scrollbar(CanvaCore, orient=VERTICAL, command=CanvaCore.yview)
# scrollbar.place(relx=1, rely=0, relheight=1, anchor=NE)
# labelCore.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, 1))

# command = onbutton.click(None, entryCore.get())

#command=lambda: click_function(entryCore.get()))

root.mainloop()
