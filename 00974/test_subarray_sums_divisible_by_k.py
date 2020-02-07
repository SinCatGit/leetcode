import unittest
from subarray_sums_divisible_by_k import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        self.assertEqual(7, solution.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))


if __name__ == '__main__':
    unittest.main()
