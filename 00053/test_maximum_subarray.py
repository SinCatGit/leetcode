import unittest
from maximum_subarray import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        self.assertEqual(6, solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
        self.assertEqual(6, solution.maxSubArraryV01([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


if __name__ == '__main__':
    unittest.main()