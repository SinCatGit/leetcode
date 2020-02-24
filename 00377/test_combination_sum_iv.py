import unittest
from combination_sum_iv import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(7, sol.combinationSum4([1, 2, 3], 4))
        self.assertEqual(0, sol.combinationSum4([3, 33, 333], 10000))

        self.assertEqual(7, sol.combinationSum4V01([1, 2, 3], 4))
        # self.assertEqual(0, sol.combinationSum4V01([3, 33, 333], 10000))


if __name__ == '__main__':
    unittest.main()
