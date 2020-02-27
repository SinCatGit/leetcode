import unittest
from count_of_range_sum import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(3, sol.countRangeSum([-2, 5, -1], -2, 2))


if __name__ == '__main__':
    unittest.main()
