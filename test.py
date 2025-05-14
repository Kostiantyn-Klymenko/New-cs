import sqlite3

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        ''')
        self.connection.commit()

    def insert_user(self, name, age):
        self.cursor.execute('''
            INSERT INTO users (name, age) VALUES (?, ?)
        ''', (name, age))
        self.connection.commit()

    def fetch_users(self):
        self.cursor.execute('SELECT * FROM users')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
# Example usage
if __name__ == "__main__":
    db = Database('users.db')
    db.create_table()
    db.insert_user('Alice', 30)
    db.insert_user('Bob', 25)

    users = db.fetch_users()
    for user in users:
        print(user)

    db.close()

