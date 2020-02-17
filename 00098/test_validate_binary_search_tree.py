import unittest
from validate_binary_search_tree import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        #          4
        #        /   \
        #       2     7
        #      / \   /
        #     1   3 5
        #            \
        #             6
        node4 = TreeNode(4)
        node2 = TreeNode(2)
        node1 = TreeNode(1)
        node3 = TreeNode(3)
        node5 = TreeNode(5)
        node6 = TreeNode(6)
        node7 = TreeNode(7)

        node4.left = node2
        node4.right = node7

        node2.left = node1
        node2.right = node3

        node7.left = node5

        node5.right = node6
        self.assertTrue(solution.isValidBST(node4))
        self.assertTrue(solution.isValidBSTV01(node4))
        #     5
        #    / \
        #   1   4
        #      / \
        #     3   6
        t25 = TreeNode(5)
        t21 = TreeNode(1)
        t24 = TreeNode(4)
        t23 = TreeNode(3)
        t26 = TreeNode(6)

        t25.left = t21
        t25.right = t24

        t24.left = t23
        t24.right = t26

        self.assertFalse(solution.isValidBST(t25))
        self.assertFalse(solution.isValidBSTV01(t25))


if __name__ == '__main__':
    unittest.main()
