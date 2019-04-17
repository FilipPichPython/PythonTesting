import unittest


def compare(a, b):
    if a > b:
        return True


class Testing(unittest.TestCase):
    def test_compare(self):
        self.assertTrue(compare(6, 1), True)

    def test_compare1(self):
        self.assertFalse(compare(1, 6), False)
