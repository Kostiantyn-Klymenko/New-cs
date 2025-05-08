from work_func import separation_line, show_products, show_basket, total, your_d_code, products, prices, num_items
import random
from tkinter import Tk, Button, Entry, StringVar, Label, messagebox, mainloop
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

window_entr = Tk()
window_entr.title("Shop")
window_entr.geometry("600x400")

label1= Label(window_entr, text="Enter your name:")

#call separation_line function
separation_line()
user_name=str(input("Please enter your name for personalised greeting: "))
separation_line()
purchasing_choice=str(input(f"Hi {user_name}\nWould you like to make a purchase?\nYes or No: ")).lower()
#checks if the user wants to use the application
while True:
    if purchasing_choice=="yes":
        print("Ok",user_name)
        #call products_list function
        main()
        #sets total_final_final to total_final
        total_final_final=total_store[0]
        print(f"Final bill:{str(total_final_final)}$")
        print("Thank you for your purchase")
        break
    elif purchasing_choice=="no":
        print("Ok, bye", user_name)
        break
    else:
        print("Error, invalid input")
        purchasing_choice=str(input("Please enter Yes or No: ")).lower()
print("END")