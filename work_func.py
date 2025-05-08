
products=["coconut", "watermelon", "orange", "lemon", "banana", "apple", "avocado", "onion", "mushroom", "peanut"]

prices=[3.5, 4.0, 2.0, 1.5, 1.0, 2.5, 5.0, 0.8, 3.0, 1.2]

num_items=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def separation_line():
    #Outputs 55 -
    print("-"*55)

def show_products():
    msg=f"\n{'Num. of items:':<15}\t{'Items:':<15}\t\t{'Price:':<10}\n"
    for counter in range(len(products)):
        msg+=(f"{counter+1:<15}\t{products[counter].capitalize():<15}\t\t{str(prices[counter])+'$':<10}\n")
    return msg

def show_basket():
    msg = f"\n{'Num. of items:':<15}\t{'Items:':<15}\t\t{'Total per item:':<10}\n"
    for counter in range(len(products)):
        if num_items[counter]>0:
            msg +=f"{num_items[counter]:<15}\t{products[counter].capitalize():<15}\t\t{str(prices[counter]*num_items[counter])+'$':<10} \n"
    msg +="Total: "+str(total())+"$"
    return msg

def add_to_basket(name, amount):
    #Adds the amount of product to the basket
    if name in products:
        num_items[products.index(name)] += amount
        msg = f"{amount} {name} added to the basket"

    else:
        msg = "Error, invalid product"
    
    return msg


def total():
    total=0
    for counter in range(len(products)):
        total+=(prices[counter]*num_items[counter])
    return total

def your_d_code():
    user_percentage=input("Please enter whatever percentage discount you want as just a number: ")
            #While loop to make sure that user_percentage is integer and in between 0 and 100
    while True:
        # Check if input is a positive integer
        if user_percentage.isdigit():
            # sets user_percentage to integer
            user_percentage = int(user_percentage)
            while True:
                if user_percentage>=0 and user_percentage<=100:
                    user_percentage/=100
                    user_percentage= 1 - user_percentage
                    break
                else:
                    print("Error, invalid percentage discount")
                    user_percentage=int(input("Please enter percentage discount between 0 and 100 as just a number: "))
            break
        else:
            print("Error, invalid data type") 
            user_percentage=input("Please enter your percentage as just a whole number: ")
    discount*=user_percentage
    return discount