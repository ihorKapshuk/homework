class Library:

    books_amount = 0

    def __init__(self, name : str):
        self.name = name
        self.books = []
        self.authors = []
    
    def __str__(self) -> str:
        return f"Name : {self.name} Books : {self.books} Authors : {self.authors}"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def new_book(self, name : str, year : int, author):
        self.books.append(str(Book(name, year, author.name)))
        self.books_amount += 1
        return Book(name, year, author.name)
    
    def group_by_author(self, author):
        sorted_list = []
        for book in self.books:
            if author.name in book:
                sorted_list.append(book)
        return sorted_list
    
    def group_by_year(self, year : int):
        sorted_list = []
        for book in self.books:
            if str(year) in book:
                sorted_list.append(book)
        return sorted_list

class Book:

    def __init__(self, name : str, year : int, author):
        self.name = name
        self.year = year
        self.author = author
    
    def __str__(self) -> str:
        return f"Name : {self.name} Year : {self.year} Author : {self.author}"
    
    def __repr__(self) -> str:
        return self.__str__()

class Author:

    def __init__(self, name : str, country : str, birthday : int, books : list):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books
    
    def __str__(self) -> str:
        return f"Name : {self.name} Country : {self.country} Birthday : {self.birthday} Books : {self.books}"
    
    def __repr__(self) -> str:
        return self.__str__()

author1 = Author("Name1", "Country1", 1950, [])
author2 = Author("Name2", "Country2", 1980, [])
library1 = Library("Odeska library")
library1.new_book("Book1", 1980, author1)
library1.new_book("Book1", 2010, author1)
library1.new_book("Book1", 2010, author2)
print(library1.books)
print(library1.group_by_author(author1))
print(library1.group_by_year(2010))
print(library1.books_amount)