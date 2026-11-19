# Parent Class
# Ito yung main class for all library materials.
class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    # Getters and setters for the basic information
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def display_info(self):
        print("Title:", self.__title)
        print("Author:", self.__author)


# Child Class: Book
# Inherits the basic information from Publication.
class Book(Publication):
    def __init__(self, title, author, number_pages):
        super().__init__(title, author)
        self.__number_pages = None
        self.set_number_of_pages(number_pages)

    def get_number_of_pages(self):
        return self.__number_pages

    def set_number_of_pages(self, number_pages):
        if number_pages > 0:
            self.__number_pages = number_pages
        else:
            print("The number of pages must be positive.")
            self.__number_pages = None

    def display_info(self):
        super().display_info()
        print("Number of Pages:", self.__number_pages)


# Child Class: Magazine
# Same inheritance, but has its own issue number.
class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = None
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, issue_number):
        if issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("The issue number must be positive.")
            self.__issue_number = None

    def display_info(self):
        super().display_info()
        print("Issue Number:", self.__issue_number)


# Creating two objects for each class
# Each object represents a different library material.

publications = [
    Publication("School Handbook", "John Smith"),
    Publication("Library Guide", "Anna Cruz")
]

books = [
    Book("Harry Potter", "J.K. Rowling", 350),
    Book("The Little Prince", "Antoine de Saint-Exupery", 96)
]

magazines = [
    Magazine("National Geographic", "Susan Goldberg", 25),
    Magazine("TIME Magazine", "Edward Felsenthal", 12)
]


# Displaying all publication information
# For loop para hindi na paulit-ulit ang display code.

print("===== PUBLICATIONS =====")
for item in publications:
    item.display_info()
    print("--------------------")

print("\n===== BOOKS =====")
for item in books:
    item.display_info()
    print("--------------------")

print("\n===== MAGAZINES =====")
for item in magazines:
    item.display_info()
    print("--------------------")
