from main_databace import *

def add_user(name, email, password):
    cur = conn.cursor()

    cur.execute("SELECT * FROM User WHERE email = ?", (email))
    existing_user = cur.fetchone()

    if existing_user:
        print("This user allready exists")
    else:
        cur.execute("SELECT userId FROM User ORDER BY userId DESC LIMIT 1")
        last_user = cur.fetchone()

        if last_user:
            last_id_num = int(last_user[0][1:]) 
            new_id = f"M{last_id_num + 1:04d}"  
        else:
            new_id = "U0001"

        cur.execute("INSERT INTO User (userId, name, email) VALUES (?, ?, ?, ?)", (new_id, name, email, password))
        conn.commit()

        print("New user added:", new_id, name, email)


def add_book(cover, title, author, genre, pub_year, rating, description):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Book WHERE title = ? AND author = ?", (title, author))
    existing_book = cur.fetchone()

    if existing_book:
        print("This book allready exists")
    else:
        cur.execute("SELECT bookId FROM Book ORDER BY bookId DESC LIMIT 1")
        last_book = cur.fetchone()

        if last_book:
            last_id_num = int(last_book[0][1:]) 
            new_id = f"B{last_id_num + 1:04d}"  
        else:
            new_id = "B0001"

        cur.execute("INSERT INTO Book (bookId, cover, title, author, genre, pub_year, rating, description) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (new_id, cover, title, author, genre, pub_year, rating))
        conn.commit()

        print("New book added:", new_id, title, author)

