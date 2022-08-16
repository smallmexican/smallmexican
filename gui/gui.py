import tkinter
from tkinter import ttk
import data
import add as add

# test request

# How to look through the data
# print(data["data"][0]["id"])

root = tkinter.Tk()
root.title('Testing Window')

pickedCrypto = tkinter.StringVar()
comboCrypto = ttk.Combobox(root, textvariable=pickedCrypto)
comboCrypto["values"] = data.get_crypto_names()
comboCrypto['state'] = 'readonly'

comboCrypto.grid(column=0, columnspan=2,row=0, pady=10, padx=2)

window_width = 400
window_height = 200

# get screen dimension

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# set the position of the window

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
#root['background'] = '#0A7E8C'
style = ttk.Style(root)
style.configure('.', font=('Comic Sans', 12))

# defining the entries as strings

def update():
    data.update_main_data()
    return print("Data Updated")

def cancel():
    root.quit()


""" Keep this as an example of event binding
    def check_price(event):
    # priceUsd
    # get the value of the coin from the name
    crypto_data = data.get_crypto_datatxt()
    value = data.get_crypto_info(crypto_data, pickedCrypto.get())
    value = value["priceUsd"]
    ttk.Label(root, text=f'The current price of your coin in £{round(float(value) * 0.83, 2)}').grid(column=0,columnspan=2)

#comboCrypto.bind('<<ComboboxSelected>>', check_price)
"""
# creating labels

# user_lbl = ttk.Label(root, text="Username: ")
# pass_lbl = ttk.Label(root, text="Password: ")
# creating entry boxes

# user_ent = ttk.Entry(root, textvariable=username)
# pass_ent = ttk.Entry(root, textvariable=password, show='*')

# creating button

add_btn = ttk.Button(root, text="Add", default="disabled", command=lambda: add.add_win(data.get_crypto_info(data.get_crypto_datatxt(), pickedCrypto.get())))
update_btn = ttk.Button(root, text="Update", command=update)
cancel_btn = ttk.Button(root, text="Cancel", command=cancel)

# positioning labels and entries and buttons oh my

update_btn.grid(column=0,row=1, pady=10, padx=2)
add_btn.grid(column=1,row=1, pady=10, padx=2)
cancel_btn.grid(column=2,row=1, pady=10, padx=2)

root.mainloop()