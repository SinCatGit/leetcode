import unittest
from paint_house import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(10, sol.minCost([[14, 2, 11], [11, 14, 5], [14, 3, 10]]))
        self.assertEqual(3, sol.minCost([[1, 2, 3], [1, 4, 6]]))


if __name__ == '__main__':
    unittest.main()
