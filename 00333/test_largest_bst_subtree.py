import unittest
from largest_bst_subtree import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        #          9
        #        /   \
        #       2     7
        #      / \   /
        #     1   3 5
        #            \
        #             6
        node4 = TreeNode(9)
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
        self.assertEqual(3, solution.largestBSTSubtree(node4))
        self.assertEqual(3, solution.largestBSTSubtreeV01(node4))
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

        self.assertEqual(5, solution.largestBSTSubtree(t25))
        self.assertEqual(5, solution.largestBSTSubtreeV01(t25))


if __name__ == '__main__':
    unittest.main()
