import unittest
from combination_sum import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(
            [[2, 2, 3], [7]],
            sorted(sol.combinationSum([2, 3, 6, 7], 7))
        )
        self.assertEqual(
            [[2, 2, 2, 2], [2, 3, 3], [3, 5]],
            sorted(sol.combinationSum([2, 3, 5], 8))
        )
        self.assertEqual(
            [[2, 2, 3], [7]],
            sorted(sol.combinationSumV01([2, 3, 6, 7], 7))
        )
        self.assertEqual(
            [[2, 2, 2, 2], [2, 3, 3], [3, 5]],
            sorted(sol.combinationSumV01([2, 3, 5], 8))
        )


if __name__ == '__main__':
    unittest.main()
