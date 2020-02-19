import unittest
from flip_binary_tree_to_match_preorder_traversal import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()

        #     2
        #    / \
        #   1   4
        #      / \
        #     3   6
        t25 = TreeNode(2)
        t21 = TreeNode(1)
        t24 = TreeNode(4)
        t23 = TreeNode(3)
        t26 = TreeNode(6)

        t25.left = t21
        t25.right = t24

        t24.left = t23
        t24.right = t26

        self.assertEqual([2], sol.flipMatchVoyage(t25, [2, 4, 3, 6, 1]))
        self.assertEqual([2, 4], sol.flipMatchVoyage(t25, [2, 1, 4, 6, 3]))


if __name__ == '__main__':
    unittest.main()
