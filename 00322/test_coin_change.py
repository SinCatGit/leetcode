import unittest
from coin_change import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        self.assertEqual(3, solution.coinChange([1, 2, 5], 11))
        self.assertEqual(5, solution.coinChange([1, 6, 7], 30))
        self.assertEqual(-1, solution.coinChange([2], 3))
        self.assertEqual(25, solution.coinChange([3, 7, 405, 436], 8839))

        self.assertEqual(3, solution.coinChangeV01([1, 2, 5], 11))
        self.assertEqual(5, solution.coinChangeV01([1, 6, 7], 30))
        self.assertEqual(-1, solution.coinChangeV01([2], 3))
        self.assertEqual(25, solution.coinChangeV01([3, 7, 405, 436], 8839))


if __name__ == '__main__':
    unittest.main()
