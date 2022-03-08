import unittest

class BookTest (unittest.TestCase):

    def test_name(self):
        self.assertEqual(("История Доколумбовых цивилизаций"), "История Доколумбовых цивилизаций")

    def test_author(self):
        self.assertEqual(("Мануэль Галич"), "Мануэль Галич")

    def test_year(self):
        self.assertEqual(("2008"), "2010")

if __name__ == '__main__':
    unittest.main()