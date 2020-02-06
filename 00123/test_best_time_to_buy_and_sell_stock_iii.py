import unittest
from best_time_to_buy_and_sell_stock_iii import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        self.assertEqual(6, solution.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
        self.assertEqual(4, solution.maxProfit([1, 2, 3, 4, 5]))
        self.assertEqual(0, solution.maxProfit([7, 6, 4, 3, 1]))

        self.assertEqual(6, solution.maxProfitV01([3, 3, 5, 0, 0, 3, 1, 4]))
        self.assertEqual(4, solution.maxProfitV01([1, 2, 3, 4, 5]))
        self.assertEqual(0, solution.maxProfitV01([7, 6, 4, 3, 1]))


if __name__ == '__main__':
    unittest.main()
