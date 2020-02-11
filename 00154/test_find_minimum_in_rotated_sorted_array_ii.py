import unittest
from find_minimum_in_rotated_sorted_array_ii import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(1, sol.findMin([1, 3, 5]))
        self.assertEqual(0, sol.findMin([2, 2, 2, 0, 1]))
        self.assertEqual(0, sol.findMin([2, 0, 1]))
        self.assertEqual(0, sol.findMin([0]))
        self.assertEqual(0, sol.findMin([1, 0]))
        self.assertEqual(0, sol.findMin([1, 1, 1, 0]))
        self.assertEqual(0, sol.findMin([0, 0]))
        self.assertEqual(0, sol.findMin([0, 0, 0]))
        self.assertEqual(1, sol.findMin([3, 1, 3, 3]))
        self.assertEqual(1, sol.findMin([3, 1, 3]))
        self.assertEqual(1, sol.findMin([1, 2, 1]))


if __name__ == '__main__':
    unittest.main()
