from work_func import show_products, show_basket, total, your_d_code, add_to_basket, remove_from_basket
import random
from tkinter import *
total_store=[0]
total_d=float(total())


def show_frame(frame):
    frame.tkraise()


def move_if_done():
    name = entry_user_name.get().strip()
    if name == "":
        label1.config(text="Error, please enter your name")
    else:
        label2.config(text=f"Hi {name}\nWould you like to make a purchase?\nYes or No: ")
        label6.config(text=f"Ok {name}\nWould you like to apply coupon?")
        show_frame(frame_buy_choice)


def yes_move():
    show_frame(frame_main)


def add():
    add_basket = Toplevel()
    add_basket.title("Add")
    add_basket.geometry("300x200")

    entry_product = Entry(add_basket, bg='lightgray')
    entry_product.pack()
    entry_quantity = Entry(add_basket, bg='lightgray')
    entry_quantity.pack()

    def get_add_message():
        result = add_to_basket(entry_product.get().lower(), int(entry_quantity.get()) )
        label_add.config(text=result)
        label_basket.config(text=show_basket())
    
    button_add = Button(add_basket, text="Add", command=get_add_message)
    button_add.pack()

    label_add = Label(add_basket, text="Add product")
    label_add.pack()

    button_close = Button(add_basket, text="Close", command=add_basket.destroy)
    button_close.pack(side=BOTTOM)

def remove():
    remove_basket = Toplevel()
    remove_basket.title("Remove")
    remove_basket.geometry("300x200")

    entry_product = Entry(remove_basket, bg='lightgray')
    entry_product.pack()
    entry_quantity = Entry(remove_basket, bg='lightgray')
    entry_quantity.pack()

    def get_remove_message():
        result = remove_from_basket(entry_product.get().lower(), int(entry_quantity.get()) )
        label_add.config(text=result)
        label_basket.config(text=show_basket())
    
    button_add = Button(remove_basket, text="Remove", command=get_remove_message)
    button_add.pack()

    label_add = Label(remove_basket, text="Remove product")
    label_add.pack()

    button_close = Button(remove_basket, text="Close", command=remove_basket.destroy)
    button_close.pack(side=BOTTOM)

def buy():
    if total() == 0:
        label_no_buy.config(text="Error, you have nothing to purchase")
    else:   
        total_store[0] = total()
        show_frame(frame_buy_choice2)


def yes_move2():
    show_frame(frame_discount)

def no_move2():
    label9.config(text=f"Final bill: {total_store[0]}$")
    show_frame(frame_end)


def discount():
    global total_d
    total_d=total()
    user_cod = entry_discount.get().strip()
    if user_cod=="HALF":
        total_d*=0.5
        show_frame(frame_end)
    elif user_cod=="RANDOM":
        random_num=round(random.uniform(0.0, 1.0), 3)
        total_d*=random_num
        show_frame(frame_end)
    elif user_cod=="YOUR":
        your_promo = Toplevel()
        your_promo.title("YOUR promo cod")
        your_promo.geometry("300x200")

        entry_percentag = Entry(your_promo, bg='lightgray')
        entry_percentag.pack()

        def get_promo_message():
            global total_d
            percentage, result = your_d_code(entry_percentag.get())
            label_promo.config(text = result)
            total_d *= percentage
            if result.startswith("Discount applied:"):
                show_frame(frame_end)
                your_promo.destroy()
        
        button_apply = Button(your_promo, text="Apply", command=get_promo_message)
        button_apply.pack()

        label_promo = Label(your_promo, text="")
        label_promo.pack()

        button_close = Button(your_promo, text="Close", command=your_promo.destroy)
        button_close.pack(side=BOTTOM)
    else:
        label_discount.config(text="Error, invalid promo cod")
    #sets total_final to rounded total_d if discoun alied 
    print(total_d)
    total_store[0] = round(total_d, 2)
    print(total_store[0])
    label9.config(text=f"Final bill: {total_store[0]}$")
    

window_app = Tk()
window_app.title("Shop")
window_app.geometry("900x600")


frame_start = Frame(window_app)
frame_buy_choice = Frame(window_app)
frame_main = Frame(window_app)
frame_buy_choice2 = Frame(window_app)
frame_discount = Frame(window_app)
frame_end = Frame(window_app)

i = 0
for frame in (frame_start, frame_buy_choice, frame_main, frame_buy_choice2, frame_discount, frame_end):
    frame.grid(row=i, column=0, sticky='nsew')
    i += 1


#Start frame
label1= Label(frame_start, text="Please enter your name for personalised greeting.")
label1.pack(side=TOP)
entry_user_name = Entry(frame_start, bg='lightgray',font=("Arial", 20))
entry_user_name.pack(side=TOP)
button_name = Button(frame_start, text="Enter", command=move_if_done)
button_name.pack(side=TOP)


#Buy choice frame
label2= Label(frame_buy_choice, text="")
label2.pack(side=TOP)
button_yes = Button(frame_buy_choice, text="Yes", command=yes_move)
button_yes.pack(side=TOP)
button_no = Button(frame_buy_choice, text="No", command=window_app.destroy)
button_no.pack(side=TOP)


#Main frame
label3= Label(frame_main, text='''User Functions:
        » Prass \"Add\" to add the product to the basket.
        » Prass \"Remove\" to remove the products from the basket.
        » Prass \"Buy\" to make the purchase.''')
label3.pack(side=TOP)
button_add = Button(frame_main, text="Add")
button_add.config(command=add)
button_add.pack(side=TOP)
button_remove = Button(frame_main, text="Remove")
button_remove.config(command=remove)
button_remove.pack(side=TOP)
button_buy = Button(frame_main, text="Buy")
button_buy.config(command=buy)
button_buy.pack(side=TOP)
label_no_buy = Label(frame_main, text="")
label_no_buy.pack(side=TOP)

frame_info = Frame(frame_main)
frame_info.pack(side=TOP)

frame_products = Frame(frame_info)
frame_products.pack(side=LEFT)

lable4= Label(frame_products, text="Products available:")
lable4.pack(side=TOP)
label_products = Label(frame_products, text=show_products())
label_products.pack(side=TOP)

frame_basket = Frame(frame_info)
frame_basket.pack(side=LEFT)

lable5= Label(frame_basket, text="Products in your basket:")
lable5.pack(side=TOP)
label_basket = Label(frame_basket, text=show_basket())
label_basket.pack(side=TOP)


#Buy choice frame 2
label6= Label(frame_buy_choice2, text=f"")
label6.pack(side=TOP)
button_yes2 = Button(frame_buy_choice2, text="Yes", command=yes_move2)
button_yes2.pack(side=TOP)
button_no2 = Button(frame_buy_choice2, text="No", command=no_move2)
button_no2.pack(side=TOP)


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
What is your promo cod?''')
label7.pack(side=TOP)
entry_discount = Entry(frame_discount, bg='lightgray')
entry_discount.pack(side=TOP)
button_discount = Button(frame_discount, text="Apply", command=discount)
button_discount.pack(side=TOP)
label_discount = Label(frame_discount, text="")
label_discount.pack()


#End frame
label8= Label(frame_end, text="Thank you for your purchase")    
label8.pack(side=TOP)
label9= Label(frame_end, text="")
label9.pack(side=TOP)
button_close = Button(frame_end, text="Close", command=window_app.destroy)
button_close.pack(side=TOP)

show_frame(frame_start)

window_app.mainloop()