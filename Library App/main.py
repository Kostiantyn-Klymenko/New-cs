from flask import Flask, render_template, request, redirect, url_for
from databse import top_books, search_books

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('home_page.html',top_books=top_books, search_books = search_books)

if __name__ == '__main__':
    app.run(debug=True)


