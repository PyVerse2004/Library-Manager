from database import Database

db = Database()
db.connect()
db.create_cursor()
db.create_table()

def add_book():
    try:
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        genre = input("Enter Genre: ")
        publication_year = int(input("Enter Year: "))
        status = input("Enter Status: ")
        db.add_book(title , author , genre , publication_year , status)

    except ValueError:
        print("Invalid Format")

    
def show_books():
    print(db.get_books())


def menu():
    while True:
        print("[1] Add Book")
        print("[2] Show Books")
        print("[3] Exit")
        try:
            inpt = int(input("Choose An Option:"))
            
            if inpt == 1:
                add_book()
            elif inpt == 2:
                show_books()
            elif inpt == 3:
                print("Good Bye")
                return 
            else:
                print("Please Enter A Valid Number")

        except ValueError:
            print("Invalid Format")
menu()