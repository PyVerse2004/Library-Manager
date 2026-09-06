from database import Database

db = Database()
db.connect()
db.create_cursor()
db.create_table()

def add_book():
    while True:
        try:
            title = input("Enter Title: ")
            if not title:
                print("Please enter a value!!!")
                return
            
            author = input("Enter Author: ")
            if not author:
                print("Please enter a value!!!")
                return
            
            genre = input("Enter Genre: ")
            if not genre:
                print("Please enter a value!!!")
                return
            
            publication_year = int(input("Enter Year: "))
            if publication_year <= 0 :
                print("Enter a correct year")
                return

            status_list = ["unread" , "reading" , "completed"]

            status = input("Enter Status (Unread , Reading , Completed): ")
            if status.lower() not in status_list:
                print("Plese Choose From Options")
                return
            
            db.add_book(title , author , genre , publication_year , status.lower())

        except ValueError:
            print("Invalid Format")
        break

    
def show_books():
    print(db.get_books())


def search_books():
    search_column = input("Search By (title , author , genre , status): ")

    if search_column.lower() == "status" :
        search_status = input("Search (unread , reading , completed) : ")
        print(db.search_by_status(search_status.lower()))
        return
    
    search_value = input(f"Find Your {search_column} : ")
    books = db.search_books(search_column , search_value)
    print(books)


def menu():
    while True:
        print("[1] Add Book")
        print("[2] Show Books")
        print("[3] Search Books")
        print("[4] Exit")
        try:
            inpt = int(input("Choose An Option:"))
            
            if inpt == 1:
                add_book()
            elif inpt == 2:
                show_books()
            elif inpt == 3:
                search_books()
            elif inpt == 4:
                print("Good Bye")
                return 
            else:
                print("Please Enter A Valid Number")

        except ValueError:
            print("Invalid Format")
menu()