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

    def search_books(self , column , value):
        allowed_column = ["title" , "author" , "genre"]

        if not column in allowed_column:
            return []

        self.cursor.execute(f"SELECT * FROM books WHERE {column} LIKE ?" , (f"%{value}%",))

        books = self.cursor.fetchall()
        return books

    def search_by_status(self , status):
        allowed_status = ["unread" , "reading" , "completed"]

        if status not in allowed_status:
            return []
        
        self.cursor.execute("SELECT * FROM books WHERE status = ?" , (status,))

        books = self.cursor.fetchall()
        return books

    def uptade_books(self , book_id , column , value):

        allowed_culomn = ["title" , "author" , "genre" , "publication_year" , "status"]

        if column not in allowed_culomn:
            return []

        self.cursor.execute(f"UPDATE books SET {column} = ? WHERE id = ?" , (value , book_id))

        self.cursor.fetchall()
        self.connection.commit()