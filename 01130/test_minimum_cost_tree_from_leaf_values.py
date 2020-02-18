import unittest
from minimum_cost_tree_from_leaf_values import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()

        self.assertEqual(32, solution.mctFromLeafValues([6, 2, 4]))
        self.assertEqual(32, solution.mctFromLeafValuesV01([6, 2, 4]))


if __name__ == '__main__':
    unittest.main()
