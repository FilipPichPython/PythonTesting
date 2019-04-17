import unittest


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('you can not do it moron!')


def growing(a):
    return a + 1


class TestClass(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(3, 9), 27)

    def test_string(self):
        self.assertEqual(multiply('a', 5), 'aaaaa')

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)

    def test_divide_by_0(self):
        self.assertEqual(divide(6, 0), print('You can not do it moron!'))

    def test_val(self):
        self.assertEqual(growing(1), 2)

    def test_val1(self):
        self.assertEqual(growing(0), 1)

    def test_val2(self):
        self.assertEqual(growing(-5), -4)


if __name__ == '__main__':
    unittest.main()
