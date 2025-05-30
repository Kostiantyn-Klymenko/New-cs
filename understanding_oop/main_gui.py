import tkinter as tk
from tkinter import messagebox
from products import Product, Coupon
from market_app import Grocessy_app

# Initialize shop and app
shop = Product()
app = Grocessy_app(id=1, shop=shop)

def refresh_products():
    products_list.delete(0, tk.END)
    for name, price in shop.get_products().items():
        products_list.insert(tk.END, f"{name}: ${price:.2f}")

def refresh_cart():
    cart_list.delete(0, tk.END)
    for item in app.cart:
        cart_list.insert(tk.END, f"{item[0]} x{item[1]} @ ${item[2]:.2f}")
    total_label.config(text=f"Total: ${app.total_price:.2f}")

def add_to_cart():
    selection = products_list.curselection()
    if not selection:
        messagebox.showwarning("No selection", "Select a product to add.")
        return
    product_line = products_list.get(selection[0])
    product_name = product_line.split(":")[0]
    try:
        qty = int(qty_entry.get())
        if qty <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid quantity", "Enter a valid quantity.")
        return
    app.add_to_cart(product_name, qty)
    refresh_cart()

def remove_from_cart():
    selection = cart_list.curselection()
    if not selection:
        messagebox.showwarning("No selection", "Select an item to remove.")
        return
    item_line = cart_list.get(selection[0])
    product_name = item_line.split(" x")[0]
    app.remove_from_cart(product_name)
    refresh_cart()

def apply_coupon():
    code = coupon_entry.get().strip().upper()
    if not code:
        messagebox.showwarning("No code", "Enter a coupon code.")
        return
    coupon = Coupon(code)
    new_total = coupon.apply(app.total_price)
    if new_total != app.total_price:
        app.update_total_price(new_total)
        refresh_cart()
        messagebox.showinfo("Coupon Applied", f"Coupon '{code}' applied!")
    else:
        messagebox.showerror("Invalid Coupon", f"Coupon '{code}' is not valid.")

def checkout():
    if not app.cart:
        messagebox.showinfo("Empty Cart", "Your cart is empty.")
        return
    app.checkout()
    refresh_cart()
    messagebox.showinfo("Checkout", "Thank you for your purchase!")

root = tk.Tk()
root.title("Grocery Shop App")

# Products Frame
products_frame = tk.LabelFrame(root, text="Products")
products_frame.pack(side=tk.LEFT, padx=10, pady=10)

products_list = tk.Listbox(products_frame, width=40, height=15)
products_list.pack(padx=5, pady=5)
refresh_products()

qty_label = tk.Label(products_frame, text="Quantity:")
qty_label.pack()
qty_entry = tk.Entry(products_frame, width=5)
qty_entry.insert(0, "1")
qty_entry.pack()

add_btn = tk.Button(products_frame, text="Add to Cart", command=add_to_cart)
add_btn.pack(pady=5)

# Cart Frame
cart_frame = tk.LabelFrame(root, text="Cart")
cart_frame.pack(side=tk.LEFT, padx=10, pady=10)

cart_list = tk.Listbox(cart_frame, width=40, height=15)
cart_list.pack(padx=5, pady=5)
total_label = tk.Label(cart_frame, text="Total: $0.00")
total_label.pack()

remove_btn = tk.Button(cart_frame, text="Remove from Cart", command=remove_from_cart)
remove_btn.pack(pady=5)

# Coupon and Checkout
coupon_frame = tk.Frame(root)
coupon_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

coupon_label = tk.Label(coupon_frame, text="Enter Coupon Code:")
coupon_label.pack()
coupon_entry = tk.Entry(coupon_frame)
coupon_entry.pack()
apply_coupon_btn = tk.Button(coupon_frame, text="Apply Coupon", command=apply_coupon)
apply_coupon_btn.pack(pady=5)

checkout_btn = tk.Button(coupon_frame, text="Checkout", command=checkout)
checkout_btn.pack(pady=20)


def save_details_as_text():
    details = []
    details.append("Cart Contents:\n")
    for item in app.cart:
        details.append(f"{item[0]} x{item[1]} @ ${item[2]:.2f}\n")
    details.append(f"\nTotal: ${app.total_price:.2f}\n")
    details.append(f"Coupon Code Used: {coupon_entry.get().strip().upper()}\n")
    with open("cart_details.txt", "w") as f:
        f.writelines(details)
    messagebox.showinfo("Saved", "Cart details saved to cart_details.txt")

# Add a button to save details
save_btn = tk.Button(coupon_frame, text="Save Details as Text", command=save_details_as_text)
save_btn.pack(pady=5)


root.mainloop()