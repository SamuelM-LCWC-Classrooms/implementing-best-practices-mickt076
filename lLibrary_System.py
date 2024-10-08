def lib_sys(books, action, title):
    if action == "view":
        print("Available books:")
        for b in books:
            if books[b]['available']:
                print(b)
    elif action == "borrow":
        if title in books and books[title]['available']:
            books[title]['available'] = False
            print(f"You have borrowed '{title}'.")
        else:
            print(f"'{title}' is not available.")
    elif action == "return":
        if title in books:
            books[title]['available'] = True
            print(f"You have returned '{title}'.")
        else:
            print(f"'{title}' does not belong to this library.")
    else:
        print("Invalid action.")

books = {
    "1984": {"available": True},
    "To Kill a Mockingbird": {"available": True},
    "The Great Gatsby": {"available": False},
    "The Catcher in the Rye": {"available": True},
    "Brave New World": {"available": True}
}

lib_sys(books, "view", "")
lib_sys(books, "borrow", "1984")
lib_sys(books, "view", "")
lib_sys(books, "return", "1984")
lib_sys(books, "view", "")
