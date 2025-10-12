import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from streak import longest_positive_streak

class TestLongestPositiveStreak(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(longest_positive_streak([]), 0)

    def test_all_positive(self):
        self.assertEqual(longest_positive_streak([1, 2, 3, 4, 5]), 5)

    def test_all_negative(self):
        self.assertEqual(longest_positive_streak([-1, -2, -3, -4, -5]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(longest_positive_streak([1, 2, -1, 3, 4, 5, 0, 6]), 3)

    def test_streak_at_end(self):
        self.assertEqual(longest_positive_streak([-1, 0, 1, 2, 3, 4]), 4)

    def test_streak_at_beginning(self):
        self.assertEqual(longest_positive_streak([1, 2, 3, 0, -1, -2]), 3)

    def test_no_positive_numbers(self):
        self.assertEqual(longest_positive_streak([0, -1, -2, -3]), 0)

    def test_single_positive_number(self):
        self.assertEqual(longest_positive_streak([1]), 1)

    def test_single_negative_number(self):
        self.assertEqual(longest_positive_streak([-1]), 0)

    def test_single_zero(self):
        self.assertEqual(longest_positive_streak([0]), 0)

    def test_multiple_streaks(self):
        self.assertEqual(longest_positive_streak([1, 2, 0, 3, 4, 5, 0, 6, 7]), 3)

    def test_example_from_prompt(self):
        self.assertEqual(longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]), 3)

if __name__ == '__main__':
    unittest.main()
