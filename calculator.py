"""
Created on Sat Oct 12 21:40:08 2019
@author: Gowtham S
"""
import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox

def process():
    try:
        number1 = tk.Entry.get(E1)
        number2 = tk.Entry.get(E2)
        number1 = int(number1)
        number2 = int(number2)
        operator = tk.Entry.get(E3)
        if operator == '+':
            ans = number1 + number2
        elif operator == '-':
            ans = number1 - number2
        elif operator == '*':
            ans = number1 * number2
        elif operator == '/':
            ans = number1 / number2
        tk.Entry.insert(E4, 0, ans)
        print(ans)
    except ValueError:
        messagebox.showwarning("Type Correct","Give Integer Values")

top = tk.Tk()
L1 = tk.Label(top, text="Calci Bitches").grid(row=0,column=1)
L2 = tk.Label(top, text="Number 1").grid(row=1,column=0)
L3 = tk.Label(top, text="Number 2").grid(row=2,column=0)
L4 = tk.Label(top, text="Operator").grid(row=3,column=0)
L5 = tk.Label(top, text="Result").grid(row=4,column=0)

E1 = tk.Entry(top, bd=5)
E1.grid(row = 1, column=1)
E2 = tk.Entry(top, bd=5)
E2.grid(row = 2, column=1)
E3 = tk.Entry(top, bd=5)
E3.grid(row = 3, column=1)
E4 = tk.Entry(top, bd=5)
E4.grid(row = 4, column=1)

B = tk.Button(top, text="Submit", command=process).grid(row=5, column=1,)

top.mainloop()

