import unittest

from os import name

class Book:
        pass

def test_name(self, book=name):
        if book.name("История Доколумбовых цивилизаций") == "История Доколумбовых цивилизаций":
            self.assertEqual(Book.b1.get_name("История Доколумбовых цивилизаций"))
            print("Is ok")
        else:
            print("Is Fail")


if __name__ == '__main__':
    unittest.main()