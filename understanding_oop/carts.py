from products import  Product
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
            print(f"{product}: ${price:.2f}")
    


shop1 = Product()
shop1.add_product("Laptop", 1200.00)
shop1.add_product("Smartphone", 800.00)
full_history = []
for user in range(1, 5):
    g1= Grocessy_app(user,shop1)
    while True:
        user_request = str(input("What do you want to do? (add/remove/show/checkout/exit/showproducts) ")).lower()
        if user_request == "add":
            product_name = str(input("Enter the product name: "))
            quantity = int(input("Enter the quantity: "))
            g1.add_to_cart(product_name, quantity)
        elif user_request == "remove":
            product_name = str(input("Enter the product name to remove: "))
            g1.remove_from_cart(product_name)
        elif user_request == "show":
            g1.show_cart()
        elif user_request == "checkout":
            g1.checkout()
        elif user_request == "exit":
            break
        elif user_request == "showproducts":
            g1.show_products()
        else:
            print("Invalid command. Please try again.")
            

    full_history.append(g1)

print("Full history of all users:")
for user in full_history:
    print(f"User {user.id}:")
    user.show_cart()