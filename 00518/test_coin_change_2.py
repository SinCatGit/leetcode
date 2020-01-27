import unittest
from coin_change_2 import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        self.assertEqual(4, solution.change(5, [1, 2, 5]))
        self.assertEqual(0, solution.change(3, [2]))
        self.assertEqual(1, solution.change(10, [10]))


if __name__ == '__main__':
    unittest.main()
