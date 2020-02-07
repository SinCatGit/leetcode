import unittest
from best_time_to_buy_and_sell_stock import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        self.assertEqual(5, solution.maxProfit([7, 1, 5, 3, 6, 4]))
        self.assertEqual(0, solution.maxProfit([7, 6, 4, 3, 1]))

        self.assertEqual(5, solution.maxProfitV01([7, 1, 5, 3, 6, 4]))
        self.assertEqual(0, solution.maxProfitV01([7, 6, 4, 3, 1]))


if __name__ == '__main__':
    unittest.main()
