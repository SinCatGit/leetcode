import unittest
from paint_house_ii import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(10, sol.minCostII([[14, 2, 11], [11, 14, 5], [14, 3, 10]]))
        self.assertEqual(5, sol.minCostII([[5]]))

        self.assertEqual(10, sol.minCostIIV01([[14, 2, 11], [11, 14, 5], [14, 3, 10]]))
        self.assertEqual(5, sol.minCostIIV01([[5]]))

        self.assertEqual(10, sol.minCostIIV02([[14, 2, 11], [11, 14, 5], [14, 3, 10]]))
        self.assertEqual(5, sol.minCostIIV02([[5]]))

        self.assertEqual(10, sol.minCostIIV03([[14, 2, 11], [11, 14, 5], [14, 3, 10]]))
        self.assertEqual(5, sol.minCostIIV03([[5]]))


if __name__ == '__main__':
    unittest.main()
