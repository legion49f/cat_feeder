import tkinter as tk

def changeState():
    global btn1
    btn1['state'] = 'normal'

mainWindow=tk.Tk()
btn1 = tk.Button(mainWindow, text='exist', state='disabled').pack()
btn2 = tk.Button(mainWindow, text='btn2', command=lambda: changeState(), state='normal').pack()

mainWindow.mainloop()