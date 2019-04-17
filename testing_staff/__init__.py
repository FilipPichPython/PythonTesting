import unittest


def multiply(a, b):
    return a * b


class TestClass(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(3, 9), 27)

    def test_string(self):
        self.assertEqual(multiply('a', 5), 'aaaaa')


if __name__ == '__main__':
    unittest.main()
