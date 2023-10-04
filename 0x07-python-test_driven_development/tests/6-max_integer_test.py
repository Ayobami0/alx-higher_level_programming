#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_end_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unorded_list(self):
        self.assertEqual(max_integer([3, 4, 1, 2]), 4)

    def test_max_beginning_list(self):
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_single_list(self):
        self.assertEqual(max_integer([1]), 1)

    def test_single_negative_list(self):
        self.assertEqual(max_integer([1, 4, 5, -6]), 5)

    def test_non_int_list(self):
        self.assertRaises(
            TypeError,
            max_integer,
            [3, 4, "This is a string", 2],
        )

    def test_all_negative_list(self):
        self.assertEqual(max_integer([-4, -1, -2, -3]), -1)

    def test_float_list(self):
        self.assertEqual(
            max_integer([3.1, 4.8, 5.4, 10.3]),
            10.3,
        )
