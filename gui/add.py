import tkinter
from tkinter import ttk

class NewWindow:
    def __init__(self, data):
        self.data = data
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
        self.window_buttons(add_window)

        add_window.mainloop()

    def window_buttons(self, root):
        for x in self.data:
            ttk.Label(root, text=f"{x} : {self.data[x]}").pack()
