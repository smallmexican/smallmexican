import tkinter
from tkinter import ttk

def add_win(data):
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
    window_buttons(add_window, data)

    add_window.mainloop()

# add window layout

def window_buttons(root, data):
    crytpo_name = ttk.Label(root,text=data['name'])
    crypto_price = ttk.Label(root, text=data['priceUsd'])
    crytpo_name.pack()
    crypto_price.pack()