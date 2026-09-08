import sqlite3

class Database:
    def connect(self):
        self.connection = sqlite3.connect("library.db")

    def create_cursor(self):
        self.cursor = self.connection.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON")

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author_id INTEGER,
            genre TEXT,
            publication_year INTEGER,
            status TEXT,
            FOREIGN KEY (author_id) REFERENCES authors(id)
                )
        """)

        self.connection.commit()

    def add_book(self , title , author_id , genre , publication_year , status):
        self.cursor.execute("""
            INSERT INTO books(title , author_id , genre , publication_year , status)
            VALUES(? , ? , ? , ? , ?)""" , (title , author_id , genre , publication_year , status))
        self.connection.commit()

    def get_books(self):
        self.cursor.execute("""
            SELECT
                books.id,
                books.title,
                authors.name,
                books.genre,
                books.publication_year,
                books.status
            FROM books
            JOIN authors
            ON books.author_id = authors.id
        """)

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

    def update_book(self , book_id , column , value):
        allowed_culomns = ["title" , "author" , "genre" , "publication_year" , "status"]

        if column not in allowed_culomns:
            return []

        self.cursor.execute(f"UPDATE books SET {column} = ? WHERE id = ?" , (value , book_id))

        self.connection.commit()

        if self.cursor.rowcount == 0:
            return False
        
        return True

    def delete_book(self , book_id):
        self.cursor.execute("DELETE FROM books WHERE id = ?" , (book_id,))

        self.connection.commit()

        if self.cursor.rowcount == 0:
            return False
        return True

    def create_authors_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS authors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            )
        """)

        self.connection.commit()

    def add_author(self , author):
        self.cursor.execute("""
            INSERT INTO authors (name)
            VALUES(?)""" , (author,))
        
        self.connection.commit()

        return self.cursor.lastrowid

    def get_authors(self):
        self.cursor.execute("SELECT id , name FROM authors")

        authors = self.cursor.fetchall()

        return authors
