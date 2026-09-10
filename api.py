from fastapi import FastAPI , HTTPException
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


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    genre: str
    publication_year: int
    status: str

@app.get("/books", response_model=list[BookResponse])
def get_books():
    books = db.get_books()

    result = []

    for book in books:
        result.append({
            "id": book[0],
            "title": book[1],
            "author": book[2],
            "genre": book[3],
            "publication_year": book[4],
            "status": book[5]
        })
    print(result)
    return result

@app.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int):

    book = db.get_book_by_id(book_id)

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return {
        "id": book[0],
        "title": book[1],
        "author": book[2],
        "genre": book[3],
        "publication_year": book[4],
        "status": book[5]
    }