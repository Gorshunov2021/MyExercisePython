import unittest
import full_name


class MyTestCase(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(
            full_name.full_name('Бурмакова',
                                'Анастасия',
                                'Владимировна'),
        'Бурмакова Анастасия Владимировна')  # add assertion here

class MyTestCase(unittest.TestCase):
    def test_big(self):
        self.assertEqual(
            full_name.full_name('БУРМАКОВА',
                                'АНАСТАСИЯ',
                                'ВЛАДИМИРОВНА'),
        'Бурмакова Анастасия Владимировна')  # add assertion here

class MyTestCase(unittest.TestCase):
    def test_small(self):
        self.assertEqual(
            full_name.full_name('бурмакова',
                                'анастасия',
                                'владимировна'),
        'Бурмакова Анастасия Владимировна')  # add assertion here

if __name__ == '__main__':
    unittest.main()
