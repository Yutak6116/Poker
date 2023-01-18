import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = tk.Tk()
root.withdraw()
window = tk.Tk()
window.grab_set()  
window.title("Input")
window.geometry('600x400')
canvas = tk.Canvas(window, width=300, height=200)
canvas.pack()
elabel = ttk.Label(window, text = 'Enter how much you want to bet in total')
canvas.create_window(0, 80, window=elabel)
entry = tk.Entry (window)
canvas.create_window(0, 100, window=entry)
much = 0

def getValue ():
    tval = entry.get()
    much = int(tval)
    wait = 0
    window.destroy()
button = tk.Button(text='Enter', command=getValue)
canvas.create_window(0, 130, window=button)

#example
window.withdraw()
messagebox.showinfo("result","PLAYER WINS POT!", parent = root)