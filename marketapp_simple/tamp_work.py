from work_func import separation_line, show_products, show_basket, total, your_d_code, products, prices, num_items
from tkinter import *

def add():
    print("Add")
    user_request2=str(input("What do you want to add? ")).lower()          
    while True:
        if user_request2 in products:
            user_request3=int(input(f"How much {user_request2.capitalize()}s do you want to add? "))
            num_items[products.index(user_request2)] += user_request3
            break
        else:
            print("Error misinput.")
            user_request2=str(input("Please enter valid product: ")).lower()

def remove():
    print("Remove") 
    user_request2=str(input("What do you want to remove? ")).lower()          
    while True:
        if user_request2 in products:
            user_request3=int(input(f"How much {user_request2.capitalize()}s do you want to remove? "))
            while True:
                if num_items[products.index(user_request2)] >= user_request3:
                    num_items[products.index(user_request2)] -= user_request3
                    break
                else:
                    print("Error you are removing more than you have renter the command.")
                    break
            break
        else:
            print("Error misinput.")
            user_request2=str(input("Please enter valid product: ")).lower()
def look():
    print("Look")
def showe():
    print("Show")   


window = Tk()
button1 = Button(window, text="Add")
button1.config(command=add)
button1.pack()
button2 = Button(window, text="Remove")
button2.config(command=remove)
button2.pack()
button3 = Button(window, text="Look")
button3.config(command=look)
button3.pack()
button4 = Button(window, text="Show")
button4.config(command=showe)
button4.pack()
window.title("Shop")
window.mainloop()
window = Tk()                   