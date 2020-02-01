import unittest
from binary_tree_right_side_view import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node5 = TreeNode(5)
        node6 = TreeNode(6)
        node7 = TreeNode(7)

        node1.left = node2
        node1.right = node3

        node2.left = node4
        node2.right = node5

        node3.left = node6
        node3.right = node7

        solution = Solution()
        self.assertEqual([1, 3, 7], solution.rightSideView(node1))


if __name__ == '__main__':
    unittest.main()
