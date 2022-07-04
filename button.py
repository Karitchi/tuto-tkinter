from tkinter import *

root = Tk()


def modify_button_text():
    label = Label(root, text="button clicked")
    label.pack()


button = Button(root, text="click here", padx=50,
                pady=20, command=modify_button_text)
button.pack()

root.mainloop()
