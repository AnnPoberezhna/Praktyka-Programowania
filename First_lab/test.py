import unittest

from Calculator import *

class TestCalculator(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(Add(""), 0)
    def test_one_param(self):
        self.assertEqual(Add("1"),1)
    def test_two_params(self):
        self.assertEqual(Add("1,10"), 11)
    def test_more_than_two_params(self):
        with self.assertRaises(ValueError):
            Add('1,2,3')

    def test_new_line_character(self):
        self.assertEqual(Add("1\n2"),3)
    def test_new_line_error(self):
        with self.assertRaises(ValueError):
            Add("5,\n")


# unittest.main(argv=['first-arg-is-ignored'], exit=False)