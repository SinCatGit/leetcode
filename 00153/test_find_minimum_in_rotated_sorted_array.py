import unittest
from find_minimum_in_rotated_sorted_array import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(1, sol.findMin([3, 4, 5, 1, 2]))
        self.assertEqual(0, sol.findMin([4, 5, 6, 7, 0, 1, 2]))
        self.assertEqual(2, sol.findMin([2]))
        self.assertEqual(1, sol.findMin([1, 2]))
        self.assertEqual(1, sol.findMin([3, 1, 2]))
        self.assertEqual(1, sol.findMin([2, 1]))


if __name__ == '__main__':
    unittest.main()
