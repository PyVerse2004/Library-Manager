from database import Database

def menu():
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    genre = input("Enter Genre: ")
    publication_year = int(input("Enter Year: "))
    status = input("Enter Status: ")

    db = Database()
    db.connect()
    db.create_cursor()
    db.create_table()
    db.add_book(title , author , genre , publication_year , status)
    print(db.get_books())


menu()