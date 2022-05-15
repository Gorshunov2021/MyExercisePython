import unittest
import Book

class BookTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_answer(self):
        self.assertEqual(Book.b3.get_answer("The Hitchhiker's Guide to the Galaxy"), "42")

    def test_str(self):
        self.assertEqual(Book.b1.__str__(), Book.b1.get_title())

    def test_show(self):
        self.assertEqual('The Colour of Magic', Book.b2.get_title())


if __name__ == '__main__':
    unittest.main()