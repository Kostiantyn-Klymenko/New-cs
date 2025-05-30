
products=["coconut", "watermelon", "orange", "lemon", "banana", "apple", "avocado", "onion", "mushroom", "peanut",'shampoo']

prices=[3.5, 4.0, 2.0, 1.5, 1.0, 2.5, 5.0, 0.8, 3.0, 1.2,50]

num_items=[0] * len(products)

class Coupon:
    def __init__(self, code):
        '''this class represents a coupon with a code, discount percentage, and name'''
        self.code = code
        self.coupon_list = {
            "DISCOUNT10": 0.10,
            "SUMMER20": 0.20,
            "WINTER15": 0.15,
            "FALL25": 0.25,
            "SPRING30": 0.30
        }

    def apply(self, amount):
        '''this method applies the coupon to the given amount'''
        if self.code in self.coupon_list:
            discount = self.coupon_list[self.code]
            discounted_amount = amount * (1 - discount)
            return discounted_amount
        else:
            print(f"Invalid coupon code: {self.code}")
            return amount

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

def remove_from_basket(name, amount):
    #Removes the amount of product from the basket
    if name in products:
            if num_items[products.index(name)] >= amount:
                num_items[products.index(name)] -= amount
                msg = f"{amount} {name} removed from the basket"  
            else:
                msg = "Error, you are removing more than you have"
    else:
        msg = "Error, invalid product"
    
    return msg

def total():
    total=0
    for counter in range(len(products)):
        total+=(prices[counter]*num_items[counter])
    return total
 
def your_d_code(user_percentage):
    # Check if input is a positive integer
    if user_percentage.isdigit():
        # sets user_percentage to integer
        user_percentage = int(user_percentage)
        if user_percentage>=0 and user_percentage<=100:
            user_percentage/=100
            user_percentage= 1 - user_percentage
            msg = f"Discount applied: {100-user_percentage*100}%"
        else:
            msg = "Error, invalid percentage discount"
    else:
        msg = "Error, invalid data type"
    return user_percentage, msg