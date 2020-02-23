import unittest
from combination_sum_ii import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(
            [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]],
            sorted(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
        )
        self.assertEqual(
            [[1, 2, 2], [5]],
            sorted(sol.combinationSum2([2, 5, 2, 1, 2], 5))
        )


if __name__ == '__main__':
    unittest.main()
