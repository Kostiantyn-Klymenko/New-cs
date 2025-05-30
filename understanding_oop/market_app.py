from products import  Product
from products import Coupon
class Grocessy_app:
    def __init__(self,id,shop):
        self.id = id
        self.cart = []
        self.total_price = 0
        self.shop = shop
    def add_to_cart(self, product_name, quantity):
        if product_name in self.shop.get_products():
            price = self.shop.get_products()[product_name]
            self.cart.append((product_name, quantity, price))
            self.total_price += price * quantity
        else:
            print(f"{product_name} not found in the shop.")
    def remove_from_cart(self, product_name):
        for item in self.cart:
            if item[0] == product_name:
                self.cart.remove(item)
                self.total_price -= item[1] * item[2]
                break
        else:
            print(f"{product_name} not found in the cart.")
    def show_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            for item in self.cart:
                print(f"{item[0]}: {item[1]} units at ${item[2]} each")
            print(f"Total price: ${self.total_price:.2f}")
    def checkout(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Checking out...")
            print(f"Total price: ${self.total_price:.2f}")
            self.cart.clear()
            self.total_price = 0
            print("Thank you for your purchase!")
    def show_products(self):
        print("Available products:")
        for product, price in self.shop.get_products().items():
            print(f"{product}: ${price:.2f}",end="||")
    def update_total_price(self, new_price):
        self.total_price = new_price
    
