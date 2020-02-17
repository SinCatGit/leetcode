import unittest
from inorder_successor_in_bst_ii import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
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

        node2.parent = node4
        node7.parent = node4

        node2.left = node1
        node2.right = node3

        node1.parent = node2
        node3.parent = node2

        node7.left = node5

        node5.parent = node7
        node5.right = node6
        node6.parent = node5

        self.assertEqual(5, sol.inorderSuccessor(node4).val)
        self.assertEqual(3, sol.inorderSuccessor(node2).val)
        self.assertEqual(6, sol.inorderSuccessor(node5).val)
        self.assertEqual(7, sol.inorderSuccessor(node6).val)
        self.assertIsNone(sol.inorderSuccessor(node7))


if __name__ == '__main__':
    unittest.main()
