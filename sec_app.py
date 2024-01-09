import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('sec_app')
window.geometry('800x500')

tk.Text(master=window).pack()

label = ttk.Label(master=window,text='hi there')
label.pack()



window.mainloop()