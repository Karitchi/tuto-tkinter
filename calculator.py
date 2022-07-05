from ast import Lambda
from audioop import mul
import tkinter as tk

root = tk.Tk()
root.title("calculator")


def button_click(number):
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, current + number)


def add():
    return


def substract():
    return


def multiply():
    return


def divide():
    return


def calculate():
    return


def clear():
    e.delete(0, tk.END)
    return


# entry caracteristic
e = tk.Entry(root, width=35, borderwidth=5)


# button caracteristic
button_7 = tk.Button(root, text=7, padx=40, pady=20,
                     command=lambda: button_click("7"))
button_8 = tk.Button(root, text=8, padx=40, pady=20,
                     command=lambda: button_click("8"))
button_9 = tk.Button(root, text=9, padx=40, pady=20,
                     command=lambda: button_click("9"))

button_4 = tk.Button(root, text=4, padx=40, pady=20,
                     command=lambda: button_click("4"))
button_5 = tk.Button(root, text=5, padx=40, pady=20,
                     command=lambda: button_click("5"))
button_6 = tk.Button(root, text=6, padx=40, pady=20,
                     command=lambda: button_click("6"))

button_1 = tk.Button(root, text=1, padx=40, pady=20,
                     command=lambda: button_click("1"))
button_2 = tk.Button(root, text=2, padx=40, pady=20,
                     command=lambda: button_click("2"))
button_3 = tk.Button(root, text=3, padx=40, pady=20,
                     command=lambda: button_click("3"))

button_0 = tk.Button(root, text=0, padx=40, pady=20,
                     command=lambda: button_click("0"))


button_clear = tk.Button(root, text="C", padx=40, pady=20, command=clear)

button_add = tk.Button(root, text="+", padx=40, pady=20, command=add)
button_substract = tk.Button(
    root, text="-", padx=40, pady=20, command=substract)
button_multiply = tk.Button(root, text="*", padx=40,
                            pady=20, command=multiply)
button_divide = tk.Button(root, text="/", padx=40,
                          pady=20, command=divide)

button_equal = tk.Button(root, text="=", padx=40,
                         pady=20, command=calculate)


# display
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_0.grid(row=5, column=0)


button_clear.grid(row=1, column=0)

button_add.grid(row=1, column=3)
button_substract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

button_equal.grid(row=5, column=3)

root.mainloop()
