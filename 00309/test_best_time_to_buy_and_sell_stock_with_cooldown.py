import unittest
from best_time_to_buy_and_sell_stock_with_cooldown import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        self.assertEqual(3, solution.maxProfit([1, 2, 3, 0, 2]))


if __name__ == '__main__':
    unittest.main()
