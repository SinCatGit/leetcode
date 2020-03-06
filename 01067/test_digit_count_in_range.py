import unittest
from digit_count_in_range import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(6, sol.digitsCount(1, 1, 13))
        self.assertEqual(5, sol.digitsCount(1, 2, 13))
        self.assertEqual(1, sol.digitsCount(2, 4, 13))
        self.assertEqual(2, sol.digitsCount(8, 4, 23))
        self.assertEqual(35, sol.digitsCount(3, 100, 250))
        self.assertEqual(36, sol.digitsCount(0, 100, 250))
        self.assertEqual(2, sol.digitsCount(0, 4, 23))


if __name__ == '__main__':
    unittest.main()
