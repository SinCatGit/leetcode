import unittest
from the_skyline_problem import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(
            [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]],
            sol.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]])
        )


if __name__ == '__main__':
    unittest.main()
