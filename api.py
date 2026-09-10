from fastapi import FastAPI
from pydantic import BaseModel
from database import Database

db = Database()
db.connect()
db.create_cursor()
db.create_authors_table()
db.create_table()

app = FastAPI()



class Book(BaseModel):
    title : str
    author_id : int
    genre : str
    publication_year : int
    status : str

@app.post("/books")
def create_book(book : Book):
    db.add_book(
        book.title,
        book.author_id,
        book.genre,
        book.publication_year,
        book.status
    )
    return book

@app.get("/books")
def get_books():
    return db.get_books()