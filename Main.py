from tkinter import *
from tkinter import ttk

app = Tk()
frm = ttk.Frame(app, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=app.destroy).grid(column=1, row=1)


app.mainloop()
