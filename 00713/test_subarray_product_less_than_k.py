import unittest
from subarray_product_less_than_k import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        self.assertEqual(8, solution.numSubarrayProductLessThanK([10, 5, 2, 6], 100))
        self.assertEqual(4, solution.numSubarrayProductLessThanK([10, 100, 2, 6], 100))


if __name__ == '__main__':
    unittest.main()