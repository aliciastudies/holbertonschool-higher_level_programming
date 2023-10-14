#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test for max_integer([..])
    """
    def test_max(self):
        """
        if list is empty
        """
        self.assertAlmostEqual(max_integer([]), None)
        """
        if int
        """
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        """
        if int at start
        """
        self.assertAlmostEqual(max_integer([6, 2, 3, 4]), 6)

        """
        if int in middle
        """
        self.assertAlmostEqual(max_integer([6, 2, 10, 3, 4]), 10)
        """
        if negative int and not biggest
        """
        self.assertAlmostEqual(max_integer([6, 2, -1, 4]), 6)
        """
        if negative int and is biggest
        """
        self.assertAlmostEqual(max_integer([-6, -2, -3, -4]), -2)
        """
        if only one element
        """
        self.assertAlmostEqual(max_integer([5]), 5)
