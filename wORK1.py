from work_func import separation_line, show_products, show_basket, total, your_d_code, products, prices, num_items
import random
from tkinter import *
total_store=[0]



def main():
    separation_line()
    print('''User Functions:
        » Write \"Add\" to add the product to the basket.
        » Write \"Look\" to view products in the basket.
        » Write \"Showe\" to view products available.
        » Write \"Buy\" to make the purchase.
        » Write \"Remove\" to remove the products from the basket.''')
    
    out_value=False
    while out_value==False:
        user_request=str(input("Write here: ")).lower()   
        while True:
            if user_request in ["add"]:
                user_request2=str(input("What do you want to add? ")).lower()          
                while True:
                    if user_request2 in products:
                        user_request3=int(input(f"How much {user_request2.capitalize()}s do you want to add? "))
                        num_items[products.index(user_request2)] += user_request3
                        break
                    else:
                        print("Error misinput.")
                        user_request2=str(input("Please enter valid product: ")).lower()
                break
            elif user_request in ["remove"]:
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
                break
            elif user_request in ["look"]:
                print("Ok opening basket...")
                separation_line()
                show_basket()
                break
            elif user_request in ["showe"]:
                print("Ok showing all products...")
                separation_line()
                show_products()
                break
            elif user_request=="buy" and total()<=0:
                print("Error you have nothing to purchase renter the command.")
                break
            elif user_request=="buy" and total()!=0:
                print("Ok...")
                separation_line()
                buying_choice=str(input("Would you like to apply coupon? \nYes or No: ")).lower()
                while True:
                    if buying_choice in ["yes"]:
                        #calls discount function
                        discount()
                        out_value=True
                        break
                    elif buying_choice in ["no"]:
                        print("Ok...")
                        #sets total_final to total if no discoun applied 
                        total_store[0]=total()
                        out_value=True
                        break
                    else:
                        print("Error, invalid input")
                        buying_choice=str(input("Please enter Yes or No: ")).lower()
                separation_line()
                break
            else:
                print("Error misinput.")
                user_request=str(input("Please enter valid command: ")).lower()
                


def discount():
    total_d=total()
    separation_line()
    print("Your promo cod:")
    print("\n")
    separation_line()
    print("⟫ -50% promo code: HALF")
    separation_line()
    print("\n")
    separation_line()
    print("⟫ -???% promo code: RANDOM")
    separation_line()
    print("\n")
    separation_line()
    print("⟫ your own % promo code: YOUR")
    separation_line()
    print("\n")
    separation_line()
    user_cod=str(input("Write your promo cod here: "))
    while True:
        if user_cod=="HALF":
            total_d*=0.5
            break
        elif user_cod=="RANDOM":
            random_num=round(random.uniform(0.0, 1.0), 3)
            total_d*=random_num
            break
        elif user_cod=="YOUR":
            total_d=your_d_code()
            break
        else:
            print("Error, invalid promo cod")
            user_cod=str(input("Please enter valid promo cod: "))
    #sets total_final to rounded total_d if discoun alied 
    total_store[0] = round(total_d, 2)

def move_if_done():
    if entry_user_name.get().strip == "":
        label2.config(text="Error, please enter your name")
    else:
        window_start.destroy()
        window_buy_choice.mainloop()

def yes_move():
    window_buy_choice.destroy()
    window_main.mainloop()

def add():
    window_main.destroy()

def remove():
    window_main.destroy()

def buy():
    window_main.destroy()

    

window_app = Tk()
window_app.title("Shop")
window_app.geometry("1200x800")


frame_start = Frame(window_app)
frame_buy_choice = Frame(window_app)
frame_main = Frame(window_app)

#Start frame
label1= Label(frame_start, text="Please enter your name for personalised greeting.")
label1.pack()
entry_user_name = Entry(frame_start)
entry_user_name.pack()
button_name = Button(frame_start, text="Enter", command=move_if_done)
button_name.pack()


#Buy choice frame
label2= Label(frame_buy_choice, text=f"Hi {entry_user_name.get()}\nWould you like to make a purchase?\nYes or No: ")
label2.pack()
button_yes = Button(frame_buy_choice, text="Yes", command=yes_move)
button_yes.pack()
button_no = Button(frame_buy_choice, text="No", command=window_app.destroy)
button_no.pack()


#Main frame
label3= Label(frame_main, text='''User Functions:
        » Write \"Add\" to add the product to the basket.
        » Write \"Remove\" to remove the products from the basket.
        » Write \"Buy\" to make the purchase.''')
label3.pack()
button_add = Button(frame_main, text="Add")
button_add.config(command=add)
button_add.pack()
button_remove = Button(frame_main, text="Remove")
button_remove.config(command=remove)
button_remove.pack()
button_buy = Button(frame_main, text="Buy")
button_buy.config(command=buy)
button_buy.pack()
lable4= Label(frame_main, text="Products available:")
lable4.pack()
label_products = Label(frame_main, text=show_products())
label_products.pack()
lable5= Label(frame_main, text="Products in your basket:")
lable5.pack()
label_basket = Label(frame_main, text=show_basket())
label_basket.pack()


window_start.mainloop()


#all separation_line function
#separation_line()
#user_name=str(input("Please enter your name for personalised greeting: "))
#separation_line()
#purchasing_choice=str(input(f"Hi {user_name}\nWould you like to make a purchase?\nYes or No: ")).lower()
#checks if the user wants to use the application
#while True:
    #if purchasing_choice=="yes":
       # print("Ok",user_name)
        #call products_list function
        #main()
        #sets total_final_final to total_final
        #total_final_final=total_store[0]
        #print(f"Final bill:{str(total_final_final)}$")
        #print("Thank you for your purchase")
       #break
    #elif purchasing_choice=="no":
        #print("Ok, bye", user_name)
        #break
   # else:
        #print("Error, invalid input")
        #purchasing_choice=str(input("Please enter Yes or No: ")).lower()
#print("END")