import unittest
import 006_Magic_Python


class BookTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_name(self):
        self.assertEqual(Book.b1.get_name(),'История Доколумбовых цивилизаций')

if __name__ == '__main__':
    unittest.main()
