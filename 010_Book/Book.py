# Kласс Book: id, Название, Автор (ы), Издательство, Год издания, Количество страниц, Цена, Тип переплета.
# Создайте класс и поля соответствующему вашему варианту (поля статические и динамические).
# Создайте три метода (класса, объекта и статический).
# Выберете поле или метод для реализации инкапсуляции.
# Пропишите запись и считывание (get, set) инкапсулированных полей.

# Создать список объектов. Вывести:
# a) список книг заданного автора;
# б) список книг, выпущенных после заданного года.

class Book:
    count = 0
    _id = 0

    def __init__(self, title, author, publisher, year, pages, price, binding):
        self._id = Book.count + 1
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.pages = pages
        self.price = price
        self.binding = binding
        Book.count += 1

    def __del__(self):
        Book.count -= 1

    def get_id(self):
        return self._id

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year

    def set_id(self, id):
        self._id = id

    def __str__(self):
        print(f"Наименование книги: {self.title}")
        return self.title


b1 = Book('The Graveyard Book', 'Neil Gaiman', 'Bloomsbury', 2008, 375, 15, 'hardback')
b2 = Book('The Colour of Magic', 'Terry Pratchett', 'Colin Smythe', 1983, 352, 11, 'paperback')
b3 = Book("The Hitchhiker's Guide to the Galaxy", 'Douglas Adams', 'Pan Books', 1979, 256, 7, 'pocketbook')
b4 = Book('Nine Princes in Amber', 'Roger Zelazny', 'Doubleday', 1970, 363, 12, 'hardback')
b5 = Book('The Stainless Steel Rat', 'Harry Harrison', 'Bantam', 1985, 377, 15, 'hardback')
b6 = Book('Shards of Honor', 'Lois McMaster Bujold', 'Baen Books', 1995, 401, 20, 'hardback')
b7 = Book("A Night in the Lonesome October", 'Roger Zelazny', 'William Morrow', 1993, 254, 7, 'pocketbook')

b1.__str__()

all_books = [b1, b2, b3, b4, b5, b6, b7]
author = str(input("Автор:  "))


#   список книг заданного автора
def all_book_by_author(my_list, author):
    print(f'Книги автора {author}: ')
    for i in range(len(my_list)):
        if my_list[i].get_author() == author:
            print(my_list[i].get_title())


#   список книг, выпущенных после заданного года
def books_published_later_then(my_list, year):
    for i in range(len(my_list)):
        if my_list[i].get_year() > year:
            print(my_list[i].get_title(), "by", my_list[i].get_author())


all_book_by_author(all_books, author)

year = int(input("Год издания:  "))
books_published_later_then(all_books, year)