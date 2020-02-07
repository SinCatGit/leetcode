import unittest
from continuous_subarray_sum import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        self.assertTrue(solution.checkSubarraySum([23, 2, 4, 6, 7], 6))
        self.assertFalse(solution.checkSubarraySum([4, 6, 7], 6))
        self.assertTrue(solution.checkSubarraySum([23, 2, 6, 4, 7], -6))
        self.assertTrue(solution.checkSubarraySum([0, 0, 4, 6, 7], 0))
        self.assertFalse(solution.checkSubarraySum([0, 1, 0], 0))


if __name__ == '__main__':
    unittest.main()
