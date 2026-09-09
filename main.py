from database import Database


db = Database()
db.connect()
db.create_cursor()
db.create_authors_table()
db.create_table()


def add_book():
    try:
        title = input("Enter Title: ").strip()

        if not title:
            print("Please enter a value!!!")
            return

        print("\nAvailable Authors:")
        for author in db.get_authors():
            print(f"[{author[0]}] {author[1]}")

        author_id = int(input("Enter Author ID: "))

        if author_id <= 0:
            print("Invalid Author ID")
            return

        if not db.author_exists(author_id):
            print("Author Not Found")
            return

        genre = input("Enter Genre: ").strip()

        if not genre:
            print("Please enter a value!!!")
            return

        publication_year = int(input("Enter Year: "))

        if publication_year <= 0:
            print("Enter a correct year")
            return

        status_list = ["unread", "reading", "completed"]

        status = input(
            "Enter Status (Unread, Reading, Completed): "
        ).lower()

        if status not in status_list:
            print("Please choose from the available options")
            return

        db.add_book(
            title,
            author_id,
            genre,
            publication_year,
            status
        )

        print("Book successfully added!")

    except ValueError:
        print("Invalid Format")


def show_books():
    books = db.get_books()

    if not books:
        print("No books found.")
        return

    for book in books:
        print(book)


def search_books():
    search_column = input(
        "Search By (title, author, genre, status): "
    ).lower()

    if search_column == "status":
        search_status = input(
            "Search (unread, reading, completed): "
        ).lower()

        books = db.search_by_status(search_status)

    elif search_column in ["title", "author", "genre"]:
        search_value = input(
            f"Find Your {search_column}: "
        ).strip()

        books = db.search_books(
            search_column,
            search_value
        )

    else:
        print("Invalid Search Option")
        return

    if not books:
        print("No books found.")
        return

    for book in books:
        print(book)


def update_book():
    try:
        column = input(
            "Choose For Update "
            "(title, author, genre, publication_year, status): "
        ).lower()

        allowed_columns = [
            "title",
            "author",
            "genre",
            "publication_year",
            "status"
        ]

        if column not in allowed_columns:
            print("Invalid Column")
            return

        book_id = int(input("Enter ID You Want: "))

        if book_id <= 0:
            print("Invalid ID")
            return

        if column == "status":
            allowed_status = [
                "unread",
                "reading",
                "completed"
            ]

            value = input("Update (unread, reading, completed): ").lower()


            if value not in allowed_status:
                print("Invalid Status")
                return
            
            db.update_book(book_id , column , value)
            return

        if column == "author":
            author = input("Update your author: ")
        
            author_id = None
        
            for i in db.get_authors():
                if author == i[1]:
                    author_id = i[0]
                    break
                
            if author_id is None:
                print("Author Not Found")
                return
        
            result = db.update_book(
                book_id,
                "author_id",
                author_id
            )
        
            if result:
                print("Author Successfully Updated")
            else:
                print("Book Not Found")
        
            return

        else:
            value = input("Update Your Value: ").strip()

            if not value:
                print("Please enter a value!!!")
                return

        result = db.update_book(
            book_id,
            column,
            value
        )

        if result:
            print("Book successfully updated!")
        else:
            print("Book Not Found")

    except ValueError:
        print("Invalid Format")


def delete_book():
    try:
        book_id = int(
            input("Enter ID You Want To Delete: ")
        )

        if book_id <= 0:
            print("Invalid ID")
            return

        result = db.delete_book(book_id)

        if result:
            print("Book Successfully Deleted")
        else:
            print("Book Not Found")

    except ValueError:
        print("Invalid Format")


def add_author():
    author_name = input("Enter Author: ").strip()

    if not author_name:
        print("Please enter a value!!!")
        return

    author_id = db.add_author(author_name)

    print(
        f"Author successfully added! "
        f"ID: {author_id}"
    )


def menu():
    while True:
        print("\n===== Personal Library Manager =====")
        print("[1] Add Book")
        print("[2] Show Books")
        print("[3] Search Book")
        print("[4] Update Book")
        print("[5] Delete Book")
        print("[6] Add Author")
        print("[7] Exit")

        try:
            choice = int(input("Choose An Option: "))

            if choice == 1:
                add_book()

            elif choice == 2:
                show_books()

            elif choice == 3:
                search_books()

            elif choice == 4:
                update_book()

            elif choice == 5:
                delete_book()

            elif choice == 6:
                add_author()

            elif choice == 7:
                print("Good Bye")
                break

            else:
                print("Please Enter A Valid Number")

        except ValueError:
            print("Invalid Format")


menu()