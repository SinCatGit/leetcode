import unittest
from two_sum_less_than_k import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(-1, sol.twoSumLessThanK([9, 8, 7], 10))
        self.assertEqual(58, sol.twoSumLessThanK([23, 35, 18, 75], 60))


if __name__ == '__main__':
    unittest.main()
