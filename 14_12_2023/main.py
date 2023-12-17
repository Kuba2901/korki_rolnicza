from library import Book,Library

def main():
    book_rental = Library("book_rent.json")
    running = True
    print("Library")
    while running:
        print("""
1. Add book
2. Delete book
3. View book
4. Rent book
5. Exit
        """)
        choice = input("> ")
        if "1" in choice:
            book_data = input("[id] [title] [author] [publish_date]: ")
            book_values = book_data.split(" ")
            book_rental.add_book(book_values[0], book_values[1], book_values[2], book_values[3])
            print("[+] Book added")
        if "2" in choice:
            id = input("[id]: ")
            if book_rental.remove_book(id):
                print("[X] Book removed")
            else:
                print("[!] No book removed")
        if "3" in choice:
            option = input("Choose what to input (id/title): ")
            if option == "id":
                id = input("[id]: ")
                book_rental.view_book(id)
            if option == "title":
                title = input("[title]: ")
                book_rental.view_book(title)
        if "4" in choice:
            id = input("[id]: ")
            available = book_rental.toggle_availability(id)

            if available is None:
                print("[!] No car with this ID")
            elif available is True:
                print("[ok] The car is back")
            else:
                print("[ok] The car was rented")
        if "5" in choice:
            running = False
main()