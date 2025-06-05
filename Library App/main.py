from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3



BOOKS_PER_PAGE = 15

app = Flask(__name__)

app.secret_key = "secret_key"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']         
        password = request.form['password']
        
        # Here you would typically check the credentials against a database
        connection = sqlite3.connect('library_database.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM User WHERE name = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        if username== user[1] and password == user[2]:
            session.clear()  # Clear any existing session data
            session['user'] = username
            print("User logged in:", username)
            return redirect('/')

    return render_template('login.html')


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    print("User logged out")
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        
        connection = sqlite3.connect('library_database.db')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM User WHERE email = ?", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            print("This user allready exists")
        else:
            cursor.execute("SELECT userId FROM User ORDER BY userId DESC LIMIT 1")
            last_user = cursor.fetchone()

            if last_user:
                last_id_num = int(last_user[0][1:]) 
                new_id = f"M{last_id_num + 1:04d}"  
            else:
                new_id = "M0001"

            cursor.execute("INSERT INTO User (userId, name, email, password) VALUES (?, ?, ?, ?)", (new_id, username, email, password,))
            print("New user added:", new_id, username, email)
            connection.commit()
            connection.close()
            session['user'] = username
            return redirect(url_for('login'))
    
    return render_template('register.html')


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
    return render_template('home_page.html',top_books=top10books, search_books = current_books,page=page,total_pages=total_pages, user=session['user'] if 'user' in session else None)


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