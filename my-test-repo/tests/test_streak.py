import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from streak import longest_positive_streak

@pytest.mark.parametrize("nums, expected", [
    ([], 0),  # Empty input
    ([1, 2, 3, 4, 5], 5), # All positive
    ([-1, -2, -3], 0), # All negative
    ([0, 0, 0], 0), # All zeros
    ([1, 2, -1, 3, 4, 5, 0, 6], 3), # Mixed with longest streak in the middle
    ([2, 3, -1, 5, 6, 7, 0, 4], 3), # Example from prompt, longest streak in the middle
    ([-1, 0, 1, 2, 3, 4], 4), # Streak at the end
    ([1, 2, 3, 0, -1, -2], 3), # Streak at the beginning
    ([1, 2, 0, 3, 4, 5, 0, 6, 7], 3), # Multiple streaks of different lengths
])
def test_longest_positive_streak(nums, expected):
    """Tests the longest_positive_streak function with various inputs."""
    assert longest_positive_streak(nums) == expected
