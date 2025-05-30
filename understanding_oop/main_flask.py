from flask import Flask, render_template, request, redirect, url_for, flash
from products import Product, Coupon
from market_app import Grocessy_app
import pickle
import os

app = Flask(__name__)
app.secret_key = "supersecret"

shop = Product()
app_obj = Grocessy_app(id=1, shop=shop)

@app.route("/", methods=["GET"])
def index():
    return render_template(
        "index.html",
        products=shop.get_products(),
        cart=app_obj.cart,
        total=app_obj.total_price,
        coupon_msg=request.args.get("coupon_msg", "")
    )

@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    name = request.form["product_name"]
    try:
        qty = int(request.form["quantity"])
        if qty <= 0:
            raise ValueError
    except ValueError:
        flash("Invalid quantity.")
        return redirect(url_for("index"))
    app_obj.add_to_cart(name, qty)
    return redirect(url_for("index"))

@app.route("/remove_from_cart", methods=["POST"])
def remove_from_cart():
    name = request.form["product_name"]
    app_obj.remove_from_cart(name)
    return redirect(url_for("index"))

@app.route("/apply_coupon", methods=["POST"])
def apply_coupon():
    code = request.form["coupon_code"].strip().upper()
    coupon = Coupon(code)
    new_total = coupon.apply(app_obj.total_price)
    if new_total != app_obj.total_price:
        app_obj.update_total_price(new_total)
        msg = f"Coupon '{code}' applied!"
    else:
        msg = f"Coupon '{code}' is not valid."
    return redirect(url_for("index", coupon_msg=msg))

@app.route("/checkout", methods=["POST"])
def checkout():
    app_obj.checkout()
    flash("Thank you for your purchase!")
    return redirect(url_for("index"))

@app.route("/save_cart", methods=["POST"])
def save_cart():
    with open("cart.pkl", "wb") as f:
        pickle.dump((app_obj.cart, app_obj.total_price), f)
    flash("Cart saved.")
    return redirect(url_for("index"))

@app.route("/load_cart", methods=["POST"])
def load_cart():
    if os.path.exists("cart.pkl"):
        with open("cart.pkl", "rb") as f:
            cart, total = pickle.load(f)
            app_obj.cart = cart
            app_obj.total_price = total
        flash("Cart loaded.")
    else:
        flash("No saved cart found.")
    return redirect(url_for("index"))

@app.route("/save_products", methods=["POST"])
def save_products():
    # save total bill with products as text file
    with open("products.txt", "w") as f:
        for product, price in shop.get_products().items():
            f.write(f"{product}: ${price:.2f}\n")
    # save products as pickle file
    with open("products.pkl", "wb") as f:
        pickle.dump(shop.get_products(), f)

@app.route("/load_products", methods=["POST"])
def load_products():
    if os.path.exists("products.pkl"):
        with open("products.pkl", "rb") as f:
            products = pickle.load(f)
            shop.products = products
        flash("Products loaded.")
    else:
        flash("No saved products found.")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)