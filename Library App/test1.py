import sqlite3

connection = sqlite3.connect('library.db')
cursor = connection.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (book_id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, rating integer, image TEXT, description TEXT, rented boolean DEFAULT 0)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)
               
''')


## make user infromation whcih book he rented
cursor.execute('''
CREATE TABLE IF NOT EXISTS rented_books (user_id INTEGER, book_id INTEGER, FOREIGN KEY(user_id) REFERENCES users(user_id), FOREIGN KEY(book_id) REFERENCES books(book_id))
''')



## insert some data into books table
cursor.execute('''
INSERT INTO books (title, author, rating, image, description) VALUES
('The Great Gatsby', 'F. Scott Fitzgerald', 5, 'https://example.com/gatsby.jpg', 'A novel set in the Roaring Twenties.'),
('To Kill a Mockingbird', 'Harper Lee', 4, 'https://example.com/mockingbird.jpg', 'A novel about racial injustice in the Deep South.'),
('1984', 'George Orwell', 5, 'https://example.com/1984.jpg', 'A dystopian novel about totalitarianism.'),
('Pride and Prejudice', 'Jane Austen', 4, 'https://example.com/pride.jpg', 'A romantic novel set in early 19th century England.')
''')


# insert into users table
cursor.execute('''
INSERT INTO users (username, password) VALUES
('john_doe', 'password123'),
('jane_doe', 'password456'),
('alice_smith', 'password789')
''')


### for usr id 1 rented book id 1
cursor.execute('''
INSERT INTO rented_books (user_id, book_id) VALUES
(1, 1),
(2, 2),
(3, 3)
''')




connection.commit()
connection.close()