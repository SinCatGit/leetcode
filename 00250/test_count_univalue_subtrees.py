import unittest
from count_univalue_subtrees import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()

        #
        #     5
        #    / \
        #   1   5
        #  / \   \
        # 5   5   5

        node1 = TreeNode(5)
        node3 = TreeNode(1)
        node2 = TreeNode(5)
        node4 = TreeNode(5)
        node5 = TreeNode(5)
        node6 = TreeNode(5)

        node1.left = node3
        node1.right = node2
        node3.left = node4
        node3.right = node5
        node2.right = node6

        self.assertEqual(4, sol.countUnivalSubtrees(node1))

        #
        #     1
        #    / \
        #   3   2
        #  / \   \
        # 4   5   6

        node1 = TreeNode(1)
        node3 = TreeNode(3)
        node2 = TreeNode(2)
        node4 = TreeNode(4)
        node5 = TreeNode(5)
        node6 = TreeNode(6)

        node1.left = node3
        node1.right = node2
        node3.left = node4
        node3.right = node5
        node2.right = node6
        sol = Solution()
        self.assertEqual(3, sol.countUnivalSubtrees(node1))


if __name__ == '__main__':
    unittest.main()
