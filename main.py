from database import Database

db = Database()
db.connect()
db.create_cursor()
db.create_table()
db.create_authors_table()
author_id = db.add_author("George Orwell")
print(author_id)

def add_book():
    while True:
        try:
            title = input("Enter Title: ")
            if not title:
                print("Please enter a value!!!")
                return
            
            author = int(input("Enter Author ID: "))
            if not author:
                print("Please enter a value!!!")
                return

            if author <= 0 :
                print("Invalid Format")
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


def update_books():
    updt_column = input(
        "Choose For Update (title , author , genre , publication_year , status) : "
    )

    if not updt_column:
        print("Please enter a value !!!")
        return

    select_id = int(input("Enter Id You Want : "))

    if not select_id:
        print("Please enter a value !!!")
        return

    if select_id <= 0:
        print("Invalid Format")
        return

    if updt_column.lower() == "status":
        allowed_value = ["unread", "reading", "completed"]

        updt_status = input(
            "Update (unread , reading , completed) : "
        )

        if updt_status.lower() not in allowed_value:
            print("Enter a valid status !!!")
            return

        result = db.update_book(
            select_id,
            updt_column.lower(),
            updt_status.lower()
        )

        if result:
            return "Book updated successfully"
        else:
            return "Book not found"

    uptd_value = input("Update Your Value : ")

    if not uptd_value:
        print("Please enter a value !!!")
        return

    result = db.update_book(
        select_id,
        updt_column.lower(),
        uptd_value
    )

    if result:
        return "Book updated successfully"
    else:
        return "Book not found"


def delete_book():
    delete_id = int(input("Enter id you want to delete: "))

    if not delete_id:
        print("Please Enter a Value !!!")
        return
    
    if delete_id <= 0 :
        print("Invalid Format !!!")
        return

    result = db.delete_book(delete_id)

    if result:
        return "Book Successfully Deleted"
    
    else:
        return "Book Not Found"


def menu():
    while True:
        print("[1] Add Book")
        print("[2] Show Books")
        print("[3] Search Book")
        print("[4] Update Book")
        print("[5] Delete Book")
        print("[6] Exit")
        try:
            inpt = int(input("Choose An Option:"))
            
            if inpt == 1:
                add_book()
            elif inpt == 2:
                show_books()
            elif inpt == 3:
                search_books()
            elif inpt == 4:
                print(update_books())
            elif inpt == 5:
               print(delete_book())    
            elif inpt == 6:
                print("Good Bye")
                return 
            else:
                print("Please Enter A Valid Number")

        except ValueError:
            print("Invalid Format")
menu()