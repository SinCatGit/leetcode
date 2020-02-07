import unittest
from subarray_sum_equals_k import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        self.assertEqual(2, solution.subarraySum([1, 1, 1], 2))
        self.assertEqual(3, solution.subarraySum([1, 2, 1, -3, 6, 1, 2], 4))
        self.assertEqual(5, solution.subarraySum([1, 1, -1, 1], 1))

        self.assertEqual(2, solution.subarraySumV01([1, 1, 1], 2))
        self.assertEqual(3, solution.subarraySumV01([1, 2, 1, -3, 6, 1, 2], 4))
        self.assertEqual(5, solution.subarraySumV01([1, 1, -1, 1], 1))


if __name__ == '__main__':
    unittest.main()
