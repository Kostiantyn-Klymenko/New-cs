
class Product:
    def __init__(self):
        self.products =  {
            "Laptop": 1200.00,
            "Smartphone": 800.00,
            "Headphones": 150.00,
            "Keyboard": 70.00,
            "Mouse": 40.00,
            "Monitor": 300.00,
            "Printer": 200.00,
            "Webcam": 90.00,
            "External Hard Drive": 110.00,
            "USB Flash Drive": 25.00,
            "Tablet": 350.00,
            "Smartwatch": 180.00,
            "Bluetooth Speaker": 60.00,
            "Wireless Charger": 35.00,
            "Router": 85.00,
            "Desk Lamp": 30.00,
            "Office Chair": 220.00,
            "Backpack": 55.00,
            "Graphics Card": 500.00,
            "Microphone": 120.00}
    def get_products(self):
        return self.products
    def add_product(self, product_name, product_price):
        self.products[product_name] = product_price
    def remove_product(self, product_name):
        if product_name in self.products:
            del self.products[product_name]
        else:
            print(f"{product_name} not found in the product list.")
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
    
        
        
    
    


