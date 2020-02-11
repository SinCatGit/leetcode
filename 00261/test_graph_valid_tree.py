import unittest
from graph_valid_tree import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertTrue(sol.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
        self.assertFalse(sol.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))


if __name__ == '__main__':
    unittest.main()
