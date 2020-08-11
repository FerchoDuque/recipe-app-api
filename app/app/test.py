from django.test import TestCase

from app.cacl import add, subtract, multiply


class CalcTest(TestCase):

    def test_add_numbers(self):
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        self.assertEqual(subtract(5, 11), 6)

    def test_multiply_numbers(self):
        self.assertEqual(multiply(5, 11), 55)
