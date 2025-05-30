import sqlite3

conn = sqlite3.connect('library_database.db')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Book ')
cur.execute('''
CREATE TABLE IF NOT EXISTS Book 
    (
    bookId TEXT PRIMARY KEY,
    cover TEXT NOT NULL,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    genre TEXT NOT NULL,
    pub_year INTEGER NOT NULL,
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5)
    );
''')

cur.execute('DROP TABLE IF EXISTS Usre ')
cur.execute('''
CREATE TABLE IF NOT EXISTS User 
    (
    userId TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
    );
''')

cur.execute('DROP TABLE IF EXISTS Loan ')
cur.execute('''
CREATE TABLE IF NOT EXISTS Loan 
    (
    userId TEXT,
    bookId TEXT,
    loanDate DATE,
    dueDate DATE NOT NULL,
    PRIMARY KEY (userId, bookId, loanDate),
    FOREIGN KEY (userId) REFERENCES User(userId),
    FOREIGN KEY (bookId) REFERENCES Books(bookId)
    );
''')

Books = [
('B0001', 'https://covers.openlibrary.org/b/id/8225631-L.jpg', 'To Kill a Mockingbird', 'Harper Lee', 'Racial Injustice', 1960, 5),
('B0002', 'https://covers.openlibrary.org/b/id/7222246-L.jpg', '1984', 'George Orwell', 'Dystopian Fiction', 1949, 5),
('B0003', 'https://covers.openlibrary.org/b/id/8224813-L.jpg', 'Pride and Prejudice', 'Jane Austen', 'Romantic Fiction', 1813, 4),
('B0004', 'https://covers.openlibrary.org/b/id/8225632-L.jpg', 'The Great Gatsby', 'F. Scott Fitzgerald', 'American Classic', 1925, 4),
('B0005', 'https://covers.openlibrary.org/b/id/6979861-L.jpg', 'The Hobbit', 'J.R.R. Tolkien', 'Fantasy', 1937, 5),
('B0006', 'https://covers.openlibrary.org/b/id/7222242-L.jpg', 'Moby Dick', 'Herman Melville', 'Adventure', 1851, 3),
('B0007', 'https://covers.openlibrary.org/b/id/7222250-L.jpg', 'War and Peace', 'Leo Tolstoy', 'Historical Fiction', 1869, 5),
('B0008', 'https://covers.openlibrary.org/b/id/8225213-L.jpg', 'Jane Eyre', 'Charlotte Brontë', 'Gothic Fiction', 1847, 4),
('B0009', 'https://covers.openlibrary.org/b/id/8231994-L.jpg', 'The Catcher in the Rye', 'J.D. Salinger', 'Coming of Age', 1951, 4),
('B0010', 'https://covers.openlibrary.org/b/id/8168691-L.jpg', 'The Lord of the Rings', 'J.R.R. Tolkien', 'Epic Fantasy', 1954, 5),
('B0011', 'https://covers.openlibrary.org/b/id/8371676-L.jpg', 'Twilight', 'Stephenie Meyer', 'Young Adult', 2005, 2),
('B0012', 'https://covers.openlibrary.org/b/id/8221257-L.jpg', 'Fifty Shades of Grey', 'E. L. James', 'Romance', 2011, 1),
('B0013', 'https://covers.openlibrary.org/b/id/8131770-L.jpg', 'The Da Vinci Code', 'Dan Brown', 'Thriller', 2003, 2),
('B0014', 'https://covers.openlibrary.org/b/id/8126181-L.jpg', 'Eragon', 'Christopher Paolini', 'Fantasy', 2002, 2),
('B0015', 'https://covers.openlibrary.org/b/id/8233779-L.jpg', 'The Alchemist', 'Paulo Coelho', 'Adventure', 1988, 1),
('B0016', 'https://covers.openlibrary.org/b/id/8370954-L.jpg', 'The Road', 'Cormac McCarthy', 'Post-Apocalyptic', 2006, 4),
('B0017', 'https://covers.openlibrary.org/b/id/8330471-L.jpg', 'The Girl with the Dragon Tattoo', 'Stieg Larsson', 'Crime', 2005, 4),
('B0018', 'https://covers.openlibrary.org/b/id/8370993-L.jpg', 'Gone Girl', 'Gillian Flynn', 'Thriller', 2012, 3),
('B0019', 'https://covers.openlibrary.org/b/id/8371640-L.jpg', 'The Fault in Our Stars', 'John Green', 'Young Adult', 2012, 4),
('B0020', 'https://covers.openlibrary.org/b/id/8370987-L.jpg', 'The Hunger Games', 'Suzanne Collins', 'Dystopian', 2008, 4),
('B0021', 'https://covers.openlibrary.org/b/id/8370988-L.jpg', 'Divergent', 'Veronica Roth', 'Dystopian', 2011, 3),
('B0022', 'https://covers.openlibrary.org/b/id/8370991-L.jpg', 'The Maze Runner', 'James Dashner', 'Dystopian', 2009, 3),
('B0023', 'https://covers.openlibrary.org/b/id/8371049-L.jpg', 'Life of Pi', 'Yann Martel', 'Adventure', 2001, 4),
('B0024', 'https://covers.openlibrary.org/b/id/8371041-L.jpg', 'Memoirs of a Geisha', 'Arthur Golden', 'Historical Fiction', 1997, 4),
('B0025', 'https://covers.openlibrary.org/b/id/8371039-L.jpg', 'The Book Thief', 'Markus Zusak', 'Historical Fiction', 2005, 5),
('B0026', 'https://covers.openlibrary.org/b/id/8371001-L.jpg', 'The Kite Runner', 'Khaled Hosseini', 'Drama', 2003, 5),
('B0027', 'https://covers.openlibrary.org/b/id/8371011-L.jpg', 'A Thousand Splendid Suns', 'Khaled Hosseini', 'Drama', 2007, 5),
('B0028', 'https://covers.openlibrary.org/b/id/8371013-L.jpg', 'The Shining', 'Stephen King', 'Horror', 1977, 4),
('B0029', 'https://covers.openlibrary.org/b/id/8371015-L.jpg', 'It', 'Stephen King', 'Horror', 1986, 4),
('B0030', 'https://covers.openlibrary.org/b/id/8371017-L.jpg', 'Carrie', 'Stephen King', 'Horror', 1974, 3),
('B0031', 'https://covers.openlibrary.org/b/id/8371019-L.jpg', 'Pet Sematary', 'Stephen King', 'Horror', 1983, 3),
('B0032', 'https://covers.openlibrary.org/b/id/8371021-L.jpg', 'The Stand', 'Stephen King', 'Post-Apocalyptic', 1978, 4),
('B0033', 'https://covers.openlibrary.org/b/id/8371023-L.jpg', 'Misery', 'Stephen King', 'Thriller', 1987, 4),
('B0034', 'https://covers.openlibrary.org/b/id/8371025-L.jpg', 'The Outsiders', 'S.E. Hinton', 'Young Adult', 1967, 4),
('B0035', 'https://covers.openlibrary.org/b/id/8371027-L.jpg', 'The Giver', 'Lois Lowry', 'Dystopian', 1993, 4),
('B0036', 'https://covers.openlibrary.org/b/id/8371029-L.jpg', 'Ender''s Game', 'Orson Scott Card', 'Science Fiction', 1985, 4),
('B0037', 'https://covers.openlibrary.org/b/id/8371031-L.jpg', 'Dune', 'Frank Herbert', 'Science Fiction', 1965, 5),
('B0038', 'https://covers.openlibrary.org/b/id/8371033-L.jpg', 'Foundation', 'Isaac Asimov', 'Science Fiction', 1951, 5),
('B0039', 'https://covers.openlibrary.org/b/id/8371035-L.jpg', 'Neuromancer', 'William Gibson', 'Cyberpunk', 1984, 4),
('B0040', 'https://covers.openlibrary.org/b/id/8371037-L.jpg', 'Snow Crash', 'Neal Stephenson', 'Cyberpunk', 1992, 4),
('B0041', 'https://covers.openlibrary.org/b/id/8371051-L.jpg', 'Ready Player One', 'Ernest Cline', 'Science Fiction', 2011, 4),
('B0042', 'https://covers.openlibrary.org/b/id/8371053-L.jpg', 'The Martian', 'Andy Weir', 'Science Fiction', 2011, 5),
('B0043', 'https://covers.openlibrary.org/b/id/8371055-L.jpg', 'The Handmaid''s Tale', 'Margaret Atwood', 'Dystopian', 1985, 4),
('B0044', 'https://covers.openlibrary.org/b/id/8371057-L.jpg', 'Oryx and Crake', 'Margaret Atwood', 'Science Fiction', 2003, 3),
('B0045', 'https://covers.openlibrary.org/b/id/8371059-L.jpg', 'Never Let Me Go', 'Kazuo Ishiguro', 'Dystopian', 2005, 3),
('B0046', 'https://covers.openlibrary.org/b/id/8371061-L.jpg', 'Cloud Atlas', 'David Mitchell', 'Science Fiction', 2004, 4),
('B0047', 'https://covers.openlibrary.org/b/id/8371063-L.jpg', 'The Time Traveler''s Wife', 'Audrey Niffenegger', 'Romance', 2003, 4),
('B0048', 'https://covers.openlibrary.org/b/id/8371065-L.jpg', 'Outlander', 'Diana Gabaldon', 'Historical Fiction', 1991, 4),
]

cur.executemany("""
INSERT OR IGNORE INTO Book (bookId, cover, title, author, genre, pub_year, rating)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", Books)

Users = [
    ('M0001', 'Alice Johnson', 'M0001@email.com', '1bcd'),
    ('M0002', 'Bob Smith', 'M0002@email.com', '3Bcd'),
    ('M0003', 'Charlie Davis', 'M0003@email.com', '6acd'),
    ('M0004', 'Diana Evans', 'M0004@email.com', 'craB'),
    ('M0005', 'Ethan Brown', 'M0005@email.com', '1234'),
    ('M0006', 'Oliver Thompson', 'M0006@email.com', '7thug3821'),
]

cur.executemany("""
INSERT OR IGNORE INTO User (userId, name, email, password)
VALUES (?, ?, ?, ?)
""", Users)

Loans = [
    ('M0001', 'B0001', '2025-02-25', '2025-03-11'),
    ('M0002', 'B0002', '2025-02-28', '2025-03-14'),
    ('M0003', 'B0004', '2025-03-01', '2025-03-15'),
    ('M0004', 'B0005', '2025-03-03', '2025-03-17'),
    ('M0006', 'B0010', '2025-03-05', '2025-03-19'),
]

cur.executemany("""
INSERT OR IGNORE INTO Loan (userId, bookId, loanDate, dueDate)
VALUES (?, ?, ?, ?)
""", Loans)

conn.commit()
conn.close()