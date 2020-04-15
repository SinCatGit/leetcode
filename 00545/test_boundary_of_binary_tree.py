import unittest
from boundary_of_binary_tree import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()

        #   1
        #    \
        #     2
        #    / \
        #   3   4

        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node1.right = node2
        node2.left = node3
        node2.right = node4
        self.assertEqual([1, 3, 4, 2], sol.boundaryOfBinaryTree(node1))
        self.assertEqual([1, 3, 4, 2], sol.boundaryOfBinaryTreeV01(node1))

        #     ____1_____
        #    /          \
        #   2            3
        #  / \          /
        # 4   5        6
        #    / \      / \
        #   7   8    9  10

        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node5 = TreeNode(5)
        node6 = TreeNode(6)
        node7 = TreeNode(7)
        node8 = TreeNode(8)
        node9 = TreeNode(9)
        node10 = TreeNode(10)

        node1.left, node1.right = node2, node3
        node2.left, node2.right = node4, node5
        node5.left, node5.right = node7, node8
        node3.left = node6
        node6.left, node6.right = node9, node10

        self.assertEqual([1, 2, 4, 7, 8, 9, 10, 6, 3], sol.boundaryOfBinaryTree(node1))
        self.assertEqual([1, 2, 4, 7, 8, 9, 10, 6, 3], sol.boundaryOfBinaryTreeV01(node1))


if __name__ == '__main__':
    unittest.main()
