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

        self.connection.commit()

    def add_book(self , title , author , genre , publication_year , status):
        self.cursor.execute("""
            INSERT INTO books(title , author , genre , publication_year , status)
            VALUES(? , ? , ? , ? , ?)""" , (title , author , genre , publication_year , status))
        self.connection.commit()

    def get_books(self):
        self.cursor.execute("SELECT * FROM books")
        books = self.cursor.fetchall()
        return books