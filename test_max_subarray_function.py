import unittest
from max_subarray_function import maximum_subarray


class TestMaximumSubarray(unittest.TestCase):
    def test_maximum_subarray_normal(self):
        actual = maximum_subarray([-2, -3, 4, -1, -2, 1, 5, -3])
        expected = 7
        self.assertEqual(actual, expected)

    def test_maximum_subarray_normal2(self):
        actual = maximum_subarray([1, 3, 8, -2, 6, -8, 5])
        expected = 16
        self.assertEqual(actual, expected)

    def test_maximum_subarray_minimum(self):
        actual = maximum_subarray([-1000000.0])
        expected = -10e4
        self.assertEqual(actual, expected)

    def test_maximum_subarray_positiveonly(self):
        actual = maximum_subarray([1, 2, 3, 4, 5])
        expected = 15
        self.assertEqual(actual, expected)

    def test_maximum_subarray_negativeonly(self):
        actual = maximum_subarray([-1, -2, -3, -4, -5])
        expected = -1
        self.assertEqual(actual, expected)