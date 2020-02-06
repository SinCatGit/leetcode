import unittest
from best_time_to_buy_and_sell_stock_with_transaction_fee import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        self.assertEqual(8, solution.maxProfit([1, 3, 2, 8, 4, 9], 2))


if __name__ == '__main__':
    unittest.main()
