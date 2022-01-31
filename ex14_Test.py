import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(200, 200)  # add assertion here

if __name__ == '__main__':
    unittest.main()
