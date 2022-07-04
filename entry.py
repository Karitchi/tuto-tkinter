from tkinter import *

root = Tk()

entry = Entry(root, width=50)
entry.pack()
entry.insert(0, "enter your name ")


def modify_button_text():
    label = Label(root, text="hello " + entry.get())
    label.pack()


button = Button(root, text="enter your name",
                command=modify_button_text, padx=50, pady=20)
button.pack()

root.mainloop()
