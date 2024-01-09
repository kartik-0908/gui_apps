import tkinter as tk
import ttkbootstrap as ttk


#window
window = tk.Tk()
window.title('simplekn')
window.geometry('300x150')

#title

title_label = ttk.Label(master=window,
                        text='hello world',font='Calibri 10 bold')
title_label.pack()

def fun():
    print('hi th')
    ans = inp_int.get()*2
    output_string.set(ans)

#input field
input_frame = ttk.Frame(master=window)
inp_int = tk.IntVar()
entry = ttk.Entry(master=input_frame,textvariable=inp_int)
button = ttk.Button(master=input_frame,text='press me',command=fun)
entry.pack(side='left',padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

#output
output_string = tk.StringVar()
output_label = ttk.Label(master=window,textvariable=output_string)
output_label.pack()

#run
window.mainloop()