from products import Product, Coupon
from market_app import Grocessy_app

shop1 = Product()

full_history = []
for user in range(1, 5):
    g1= Grocessy_app(user,shop1)
    while True:
        user_request = str(input("What do you want to do? (add/remove/show/checkout/exit/showproducts) ")).lower()
        if user_request == "add":
            g1.show_products()
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
    
    wish = input('do you want to apply a coupon? (yes/no): ')
    if wish.lower() == 'yes':
        coupon_code = input('Enter the coupon code: ')
        coupon = Coupon(coupon_code)
        new_price = coupon.apply(g1.total_price)
        g1.update_total_price(new_price)
    else:
        print("No coupon applied.")
    
    full_history.append(g1)
    print(f"User {user} total price after coupon: ${g1.total_price:.2f}")

print("Full history of all users:")
for user in full_history:
    print(f"User {user.id}:")
    user.show_cart()