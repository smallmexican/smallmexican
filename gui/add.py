import tkinter
from tkinter import ttk

class Add:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def add():
    add_window = tkinter.Tk()
    add_window.title("Add New Crypto")
    window_width = 400
    window_height = 200
    screen_width = add_window.winfo_screenwidth()
    screen_height = add_window.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    # get screen dimension
    add_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


    add_window.mainloop()

