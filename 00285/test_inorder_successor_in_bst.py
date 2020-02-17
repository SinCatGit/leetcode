import unittest
from inorder_successor_in_bst import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        #          4
        #        /   \
        #       2     7
        #      / \   /
        #     1   3 5
        node4 = TreeNode(4)
        node2 = TreeNode(2)
        node1 = TreeNode(1)
        node3 = TreeNode(3)
        node5 = TreeNode(5)
        node7 = TreeNode(7)

        node4.left = node2
        node4.right = node7

        node2.left = node1
        node2.right = node3

        node7.left = node5

        self.assertEqual(7, sol.inorderSuccessor(node4, node5).val)
        self.assertEqual(7, sol.inorderSuccessorV01(node4, node5).val)
        self.assertEqual(7, sol.inorderSuccessorV02(node4, node5).val)


if __name__ == '__main__':
    unittest.main()
