import unittest
from best_time_to_buy_and_sell_stock_iv import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        self.assertEqual(2, solution.maxProfit(2, [2, 4, 1]))
        self.assertEqual(5, solution.maxProfit(2, [2, 4, 1, 4, 3, 4]))
        self.assertEqual(6, solution.maxProfit(4, [2, 4, 1, 4, 3, 4]))
        self.assertEqual(7, solution.maxProfit(2, [3, 2, 6, 5, 0, 3]))
        self.assertEqual(0, solution.maxProfit(2, [7, 6, 4, 3, 1]))


if __name__ == '__main__':
    unittest.main()
