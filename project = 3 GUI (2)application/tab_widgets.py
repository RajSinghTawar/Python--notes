# notebook -- containt two pages
# page1               page2
# widgets             widgets

import tkinter as tk
from tkinter  import Entry, Frame, Label, ttk
win = tk.Tk()
win.title('TAB Control')

nb = ttk.Notebook(win)
page1 = Frame(nb)
page2 = Frame(nb)
nb.add(page1, text='ONE')
nb.add(page2, text='TWO')
# nb.grid(row=0, column=0)
nb.pack(expand=True, fill='both')


label1 = ttk.Label(page1, text='This is label: ')
label1.grid(row=0, column=0)

entry1 = ttk.Entry(page1, width=26)
entry1.grid(row=0, column=1)

label2 = ttk.Label(page2, text='This is label: ')
label2.grid(row=0, column=0)

win.mainloop()
