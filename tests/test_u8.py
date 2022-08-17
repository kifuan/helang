import unittest

from helang.u8 import U8
from helang.exceptions import CyberSubtractionException


class TestU8(unittest.TestCase):
    def setUp(self) -> None:
        self.a = U8([5, 3, 6])
        self.b = U8([2, 6, 7])
        self.c = U8([2])
        self.a_b = [3, -3, -1]
        self.b_a = [-3, 3, 1]
        self.a_c = [3, 1, 4]
        self.b_c = [0, 4, 5]

    def test_u8_subtraction(self):
        self.assertEqual(self.a - self.b, self.a_b)
        self.assertEqual(self.b - self.a, self.b_a)
        self.assertEqual(self.a - self.c, self.a_c)
        self.assertEqual(self.b - self.c, self.b_c)

        try:
            self.c - self.a
            self.fail('illegal operation: number - vector')
        except CyberSubtractionException:
            ...

    def test_u8_compare(self):
        self.assertEqual(self.a, self.a)
        self.assertEqual(self.a, self.a.value)
        self.assertNotEqual(self.a, self.b)
