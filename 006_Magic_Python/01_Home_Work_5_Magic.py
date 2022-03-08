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

    def __init__(self, name, author, publishing_house, year, number_of_pages, price, binding_type):
        self._id = Book.count + 1
        self.name = name
        self.author = author
        self.publishing_house = publishing_house
        self.year = year
        self.number_of_pages = number_of_pages
        self.price = price
        self.binding_type = binding_type
        Book.count += 1

    def __del__(self):
        Book.count -= 1

    def get_id(self):
        return self._id

    def get_name(self):
        return self.name

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year

    def set_id(self, id):
        self._id = id

    def __str__(self):
        print(f"Наименование книги: {self.name}")
        return self.name

b1 = Book('История Доколумбовых цивилизаций', 'Мануэль Галич', 'Мысль', 1990, 410, 345, 'Твердый переплет')
b2 = Book('Древние цивилизации Америки', 'Гуляев В.И', 'Вече', 2008, 448, 74, 'Твердый переплет')
b3 = Book("История Древнего Египта", 'Перепёлкин Ю.Я.', 'Нева', 2000, 560, 104, 'Мягкий переплет')
b4 = Book('Пьесы писателей Латинской Америки (сборник)', 'Мануэль Галич', 'Искусство', 1970, 200, 76, 'hardback')
b5 = Book('Шумер. Вавилон. Ассирия: 5000 лет истории', 'Гуляев В.И', 'Алетейя', 2004, 440, 66, 'hardback')
b6 = Book('Хозяйство староегипетских вельмож', 'Перепёлкин Ю.Я.', 'Наука', 1988, 304, 87, 'hardback')

b1.__str__()

all_books = [b1, b2, b3, b4, b5, b6]
author = str(input("Автор:  "))


#   список книг заданного автора
def all_book_by_author(my_list, author):
    print(f'Книги автора {author}: ')
    for i in range(len(my_list)):
        if my_list[i].get_author() == author:
            print("\n", my_list[i].get_name())
            print("Год издания: ", my_list[i].get_year())

#   список книг, выпущенных после заданного года
def books_published_later_then(my_list, year):
    for i in range(len(my_list)):
        if my_list[i].get_year() > year:
            print(my_list[i].get_name(), "by", my_list[i].get_author())

all_book_by_author(all_books, author)
print("\n")
year = int(input("Введите год издания и вы увидите список книг из библиотеки выше указанного года:  "))
books_published_later_then(all_books, year)
