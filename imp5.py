
class Publisher:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Publisher Name:", self.name)


class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author

    def display(self):
        super().display()
        print("Book Title:", self.title)
        print("Author:", self.author)


class Python(Book):
    def __init__(self, name, title, author, price, no_of_pages):
        super().__init__(name, title, author)
        self.price = price
        self.no_of_pages = no_of_pages

    def display(self):
        super().display()
        print("Price:", self.price)
        print("Number of Pages:", self.no_of_pages)


# Get input from user
name = input("Enter publisher name: ")
title = input("Enter book title: ")
author = input("Enter author name: ")
price = float(input("Enter book price: "))
pages = int(input("Enter number of pages: "))

# Create object
p = Python(name, title, author, price, pages)

# Display information
print("\nPython Book Details")
p.display()

