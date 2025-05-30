
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price      

available_products = {
    "coconut": Product("coconut", 1.50),
    "watermelon": Product("watermelon", 2.00),
    "orange": Product("orange", 0.50),
    "lemon": Product("lemon", 0.75),
    "banana": Product("banana", 0.25),
    "apple": Product("apple", 0.30),
    "avocado": Product("avocado", 1.00),
    "onion": Product("onion", 0.40),
    "mushroom": Product("mushroom", 0.60),
    "peanut": Product("peanut", 0.20),
    "shampoo": Product("shampoo", 5.00),
}
        
class Coupon:   
    def __init__(self, code, discount_percent, label):
        self.code = code
        self.discount_percent = discount_percent
        self.label = label

    def apply(self, code, total):
        if code in available_promos:
            coupon = available_promos[code]
            return round (total * (1 - coupon.discount_percent), 2)
        else:
            print(f"Error invalid coupon code: {code}")
            return total

available_promos = {
    "HALF": Coupon("HALF", 0.5, "50% off"),
    "WElCOME": Coupon("WELCOME", 0.2, "20% off"),
}

class Grocessy_app:
    def __init__(self,id,shop):
        self.id = id
        self.cart = []
        self.total_price = 0
        self.shop = shop
    def add_to_cart(self, product_name, quantity):
        if product_name in available_products:
            price = available_products[product_name].price
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