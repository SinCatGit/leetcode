import unittest
from combination_sum_iii import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(
            [[1, 2, 4]],
            sorted(sol.combinationSum3(3, 7))
        )
        self.assertEqual(
            [[1, 2, 6], [1, 3, 5], [2, 3, 4]],
            sorted(sol.combinationSum3(3, 9))
        )

        self.assertEqual(
            [[1, 2, 4]],
            sorted(sol.combinationSum3V01(3, 7))
        )
        self.assertEqual(
            [[1, 2, 6], [1, 3, 5], [2, 3, 4]],
            sorted(sol.combinationSum3V01(3, 9))
        )


if __name__ == '__main__':
    unittest.main()
