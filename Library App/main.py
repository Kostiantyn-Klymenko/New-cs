from flask import Flask, render_template, request, redirect, url_for
import sqlite3


BOOKS_PER_PAGE = 15

app = Flask(__name__)



@app.route('/')
def index():     
    connection = sqlite3.connect('library_database.db')
    cursor = connection.cursor()
    data = cursor.execute('select * from Book')
    data = data.fetchall()
    all_books = []
    for row in data:
        all_books.append(
            {
                'bookId':row[0],
                'cover_image':row[1],
                'title':row[2],
                'author':row[3],
                'rating':row[6],
                'topic':row[4]
            }
        )
        page = request.args.get('page',1,type=int)
        start = (page - 1) * BOOKS_PER_PAGE
        end = start + BOOKS_PER_PAGE
        current_books = all_books[start:end]
        total_pages  = len(all_books) // BOOKS_PER_PAGE


        
    data10 = cursor.execute('select * from Book ORDER BY rating desc limit 10')
    data10 = data10.fetchall()
    top10books = []
    for row in data10:
        top10books.append(
            {
                'cover_image':row[1],
                'title':row[2],
                'author':row[3],
                'rating':row[6],
                'topic':row[4]
            }
        )
    return render_template('home_page.html',top_books=top10books, search_books = current_books,page=page,total_pages=total_pages)


@app.route("/<string:BookId>")
def book_page(BookId):
    connection = sqlite3.connect('library_database.db')
    cursor = connection.cursor()
    perticular_book = cursor.execute('SELECT * FROM Book WHERE bookId = ?', (BookId,)).fetchone()
    print(perticular_book)

    
    the_book =  {
                'cover_image':perticular_book[1],
                'title':perticular_book[2],
                'author':perticular_book[3],
                'rating':perticular_book[6],
                'topic':perticular_book[4],
                'year':perticular_book[5],
                'description':perticular_book[7]
            }
        

    data10 = cursor.execute('SELECT * FROM Book ORDER BY rating DESC LIMIT 10')
    data10 = data10.fetchall()

    top10books = []
    for row in data10:
        top10books.append(
            {
                'cover_image':row[1],
                'title':row[2],
                'author':row[3],
                'rating':row[6],
                'topic':row[4]
            }
        )
        
    return render_template('book_page.html',the_book=the_book, top_books=top10books)

if __name__ == '__main__':
    app.run(debug=True)