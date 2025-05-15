from work_func import separation_line, show_products, show_basket, total, your_d_code, products, prices, num_items, add_to_basket
import random
from tkinter import Tk, Button, Entry, StringVar, Label, messagebox, mainloop
total_store=[0]


def get_add_message():
    result= add_to_basket(entry_name.get(), int(entry_quantity.get()) )
    label_add.config(text=result)

def show_full_basket():
    msg = show_basket()
    label_basket.config(text=msg)

separation_line()
print('''User Functions:
    » Write \"Add\" to add the product to the basket.
    » Write \"Look\" to view products in the basket.
    » Write \"Showe\" to view products available.
    » Write \"Buy\" to make the purchase.
    » Write \"Remove\" to remove the products from the basket.''')


windows = Tk()
windows.title("Shop")
windows.geometry("600x400")





entry_name = Entry(windows, font=("Arial", 12), width=20)
entry_name.pack()
entry_quantity = Entry(windows, font=("Arial", 12), width=20)
entry_quantity.pack()



button_add = Button(windows, text="Add", command=get_add_message, width=10, height=2)
button_add.pack()

label_add = Label(windows, text="Add product", font=("Arial", 12), width=20)
label_add.pack()

button_b = Button(windows, text="Basket", command=show_full_basket, width=10, height=2)
button_b.pack()

label_basket = Label(windows, text='', font=("Arial", 12), width=20)
label_basket.pack()

mainloop()



