import unittest
from verify_preorder_sequence_in_binary_search_tree import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertFalse(sol.verifyPreorder([5, 2, 6, 1, 3]))
        self.assertTrue(sol.verifyPreorder([5, 2, 1, 3, 6]))

        self.assertFalse(sol.verifyPreorderV01([5, 2, 6, 1, 3]))
        self.assertTrue(sol.verifyPreorderV01([5, 2, 1, 3, 6]))

        self.assertFalse(sol.verifyPreorderV02([5, 2, 6, 1, 3]))
        self.assertTrue(sol.verifyPreorderV02([5, 2, 1, 3, 6]))


if __name__ == '__main__':
    unittest.main()
