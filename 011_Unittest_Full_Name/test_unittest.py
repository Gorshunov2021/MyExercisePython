import unittest
import self

from full_name import full_name


class NameTestCase(unittest.TestCase):

    def test_first_last_name(self):

        format_name = full_name('Бурмакова', 'Анастасия')
        self.assertEqual(format_name, 'Бурмакова Анастасия')

    def test_first_last_middle(self):

        format_name = full_name('Бурмакова', 'Анастасия', 'Владимировна')
        self.assertEqual(format_name, 'Бурмакова Анастасия Владимировна')


if __name__ == '__main__':
    unittest.main()
