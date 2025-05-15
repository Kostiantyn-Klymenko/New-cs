from work_func import show_products, show_basket, total, your_d_code, add_to_basket, remove_from_basket
import random
from tkinter import *
from tkinter import ttk

total_store = [0]
total_d = [0]

def show_frame(frame):
    frame.tkraise()

def move_if_done():
    name = entry_user_name.get().strip()
    if name == "":
        label1.config(text="Error, please enter your name", fg="red")
    else:
        label2.config(text=f"Hi {name}\nWould you like to make a purchase?\nYes or No: ", fg="black")
        label6.config(text=f"Ok {name}\nWould you like to apply a coupon?")
        show_frame(frame_buy_choice)

def yes_move():
    show_frame(frame_main)

def add():
    add_basket = Toplevel()
    add_basket.title("Add Product")
    add_basket.geometry("300x250")
    add_basket.configure(bg="#f0f0f0")

    Label(add_basket, text="Enter Product:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
    entry_product = Entry(add_basket, bg='lightgray')
    entry_product.pack(pady=5)

    Label(add_basket, text="Enter Quantity:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
    entry_quantity = Entry(add_basket, bg='lightgray')
    entry_quantity.pack(pady=5)

    def get_add_message():
        result = add_to_basket(entry_product.get().lower(), int(entry_quantity.get()))
        label_add.config(text=result)
        label_basket.config(text=show_basket())

    button_add = Button(add_basket, text="Add", command=get_add_message, bg="#4CAF50", fg="white", font=("Arial", 10))
    button_add.pack(pady=10)

    label_add = Label(add_basket, text="", bg="#f0f0f0", font=("Arial", 10))
    label_add.pack()

    button_close = Button(add_basket, text="Close", command=add_basket.destroy, bg="#f44336", fg="white", font=("Arial", 10))
    button_close.pack(side=BOTTOM, pady=10)

def remove():
    remove_basket = Toplevel()
    remove_basket.title("Remove Product")
    remove_basket.geometry("300x250")
    remove_basket.configure(bg="#f0f0f0")

    Label(remove_basket, text="Enter Product:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
    entry_product = Entry(remove_basket, bg='lightgray')
    entry_product.pack(pady=5)

    Label(remove_basket, text="Enter Quantity:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
    entry_quantity = Entry(remove_basket, bg='lightgray')
    entry_quantity.pack(pady=5)

    def get_remove_message():
        result = remove_from_basket(entry_product.get().lower(), int(entry_quantity.get()))
        label_remove.config(text=result)
        label_basket.config(text=show_basket())

    button_remove = Button(remove_basket, text="Remove", command=get_remove_message, bg="#4CAF50", fg="white", font=("Arial", 10))
    button_remove.pack(pady=10)

    label_remove = Label(remove_basket, text="", bg="#f0f0f0", font=("Arial", 10))
    label_remove.pack()

    button_close = Button(remove_basket, text="Close", command=remove_basket.destroy, bg="#f44336", fg="white", font=("Arial", 10))
    button_close.pack(side=BOTTOM, pady=10)

def buy():
    if total() == 0:
        label_no_buy.config(text="Error, you have nothing to purchase", fg="red")
    else:
        total_store[0] = total()
        show_frame(frame_buy_choice2)

def yes_move2():
    show_frame(frame_discount)

def no_move2():
    label9.config(text=f"Final bill: {total_store[0]}$", font=("Arial", 14))
    show_frame(frame_end)

def discount():
    global total_d
    total_d[0] = total()
    user_cod = entry_discount.get().strip()
    if user_cod == "HALF":
        total_d[0] *= 0.5
        show_frame(frame_end)
    elif user_cod == "RANDOM":
        random_num = round(random.uniform(0.0, 1.0), 3)
        total_d[0] *= random_num
        show_frame(frame_end)
    elif user_cod == "YOUR":
        your_promo = Toplevel()
        your_promo.title("YOUR Promo Code")
        your_promo.geometry("300x200")
        your_promo.configure(bg="#f0f0f0")

        Label(your_promo, text="Enter Discount Percentage:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
        entry_percentag = Entry(your_promo, bg='lightgray')
        entry_percentag.pack(pady=5)

        def get_promo_message():
            global total_d
            percentage, result = your_d_code(entry_percentag.get())
            label_promo.config(text=result, fg="green" if result.startswith("Discount applied:") else "red")
            if result.startswith("Discount applied:"):
                total_d[0] *= percentage
                total_store[0] = round(total_d[0], 2)
                label9.config(text=f"Final bill: {total_store[0]}$", font=("Arial", 14))
                show_frame(frame_end)
                your_promo.destroy()

        button_apply = Button(your_promo, text="Apply", command=get_promo_message, bg="#4CAF50", fg="white", font=("Arial", 10))
        button_apply.pack(pady=10)

        label_promo = Label(your_promo, text="", bg="#f0f0f0", font=("Arial", 10))
        label_promo.pack()

        button_close = Button(your_promo, text="Close", command=your_promo.destroy, bg="#f44336", fg="white", font=("Arial", 10))
        button_close.pack(side=BOTTOM, pady=10)
    else:
        label_discount.config(text="Error, invalid promo code", fg="red")

    total_store[0] = round(total_d[0], 2)
    label9.config(text=f"Final bill: {total_store[0]}$", font=("Arial", 14))

# Main Window
window_app = Tk()
window_app.title("Shop")
window_app.geometry("1000x700")
window_app.configure(bg="#f0f0f0")
window_app.resizable(False, False)

# Frames
frame_start = Frame(window_app, bg="#f0f0f0")
frame_buy_choice = Frame(window_app, bg="#f0f0f0")
frame_main = Frame(window_app, bg="#f0f0f0")
frame_buy_choice2 = Frame(window_app, bg="#f0f0f0")
frame_discount = Frame(window_app, bg="#f0f0f0")
frame_end = Frame(window_app, bg="#f0f0f0")

for frame in (frame_start, frame_buy_choice, frame_main, frame_buy_choice2, frame_discount, frame_end):
    frame.grid(row=0, column=0, sticky='nsew')

# Start Frame
label1 = Label(frame_start, text="Please enter your name for a personalized greeting.", bg="#f0f0f0", font=("Arial", 14))
label1.pack(pady=20)
entry_user_name = Entry(frame_start, bg='lightgray', font=("Arial", 12))
entry_user_name.pack(pady=10)
button_name = Button(frame_start, text="Enter", command=move_if_done, bg="#4CAF50", fg="white", font=("Arial", 12))
button_name.pack(pady=10)

#Buy choice frame
label2= Label(frame_buy_choice, text="", bg="#f0f0f0", font=("Arial", 14))
label2.pack(pady=20)
button_yes = Button(frame_buy_choice, text="Yes", command=yes_move, bg="#4CAF50", fg="white", font=("Arial", 12))
button_yes.pack(pady=10)
button_no = Button(frame_buy_choice, text="No", command=window_app.destroy, bg="#f44336", fg="white", font=("Arial", 12))
button_no.pack(pady=10)

#Main frame
label3= Label(frame_main, text='''User Functions:
        » Prass \"Add\" to add the product to the basket.
        » Prass \"Remove\" to remove the products from the basket.
        » Prass \"Buy\" to make the purchase.''', bg="#f0f0f0", font=("Arial", 14))
label3.pack(pady=20)
button_add = Button(frame_main, text="Add", command=add, bg="#4CAF50", fg="white", font=("Arial", 12))
button_add.pack(pady=10)
button_remove = Button(frame_main, text="Remove", command=remove, bg="#4CAF50", fg="white", font=("Arial", 12))
button_remove.pack(pady=10)
button_buy = Button(frame_main, text="Buy", command=buy, bg="#4CAF50", fg="white", font=("Arial", 12))
button_buy.pack(pady=10)
label_no_buy = Label(frame_main, text="", bg="#f0f0f0", font=("Arial", 14))
label_no_buy.pack(pady=10)

frame_info = Frame(frame_main, bg="#f0f0f0")
frame_info.pack(pady=20)

frame_products = Frame(frame_info, bg="#f0f0f0")
frame_products.pack(side=LEFT, padx=20)

lable4= Label(frame_products, text="Products available:", bg="#f0f0f0", font=("Arial", 14))
lable4.pack(pady=10)
label_products = Label(frame_products, text=show_products(), bg="#f0f0f0", font=("Arial", 12))
label_products.pack(pady=10)

frame_basket = Frame(frame_info, bg="#f0f0f0")
frame_basket.pack(side=LEFT, padx=20)

lable5= Label(frame_basket, text="Products in your basket:", bg="#f0f0f0", font=("Arial", 14))
lable5.pack(pady=10)
label_basket = Label(frame_basket, text=show_basket(), bg="#f0f0f0", font=("Arial", 12))
label_basket.pack(pady=10)

#Buy choice frame 2
label6= Label(frame_buy_choice2, text="", bg="#f0f0f0", font=("Arial", 14))
label6.pack(pady=20)
button_yes2 = Button(frame_buy_choice2, text="Yes", command=yes_move2, bg="#4CAF50", fg="white", font=("Arial", 12))
button_yes2.pack(pady=10)
button_no2 = Button(frame_buy_choice2, text="No", command=no_move2, bg="#f44336", fg="white", font=("Arial", 12))
button_no2.pack(pady=10)

#Discount frame
label7= Label(frame_discount, text='''Your promo cods:
              
-------------------------------------------------------
⟫ -50% promo code: HALF
-------------------------------------------------------


-------------------------------------------------------
⟫ -???% promo code: RANDOM
-------------------------------------------------------


-------------------------------------------------------
⟫ your own % promo code: YOUR
-------------------------------------------------------


-------------------------------------------------------
What is your promo cod?''', bg="#f0f0f0", font=("Arial", 14))
label7.pack(pady=20)
entry_discount = Entry(frame_discount, bg='lightgray', font=("Arial", 12))
entry_discount.pack(pady=10)
button_discount = Button(frame_discount, text="Apply", command=discount, bg="#4CAF50", fg="white", font=("Arial", 12))
button_discount.pack(pady=10)
label_discount = Label(frame_discount, text="", bg="#f0f0f0", font=("Arial", 14))
label_discount.pack(pady=10)

#End frame
label8= Label(frame_end, text="Thank you for your purchase", bg="#f0f0f0", font=("Arial", 14))    
label8.pack(pady=20)
label9= Label(frame_end, text="", bg="#f0f0f0", font=("Arial", 14))
label9.pack(pady=10)
button_close = Button(frame_end, text="Close", command=window_app.destroy, bg="#f44336", fg="white", font=("Arial", 12))
button_close.pack(pady=10)

show_frame(frame_start)

window_app.mainloop()