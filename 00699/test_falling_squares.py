import unittest
from falling_squares import Solution


class TestSolution(unittest.TestCase):
    def test_TwoSum_Solution(self):
        sol = Solution()
        self.assertEqual([2, 5, 5, 5], sol.fallingSquares([[1, 2], [2, 3], [6, 1], [5, 2]]))


if __name__ == '__main__':
    unittest.main()
