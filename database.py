import sqlite3

class Database:
    def connect(self):
        self.connection = sqlite3.connect("library.db")

    def create_cursor(self):
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        genre TEXT,
        publication_year INTEGER,
        status TEXT
    )
""")


db = Database()
db.connect()
db.create_cursor()
