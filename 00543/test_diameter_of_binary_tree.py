import unittest
from diameter_of_binary_tree import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node5 = TreeNode(5)
        node1.left = node2
        node1.right = node3
        node2.left = node4
        node2.right = node5
        solution = Solution()
        self.assertEqual(3, solution.diameterOfBinaryTree(node1))


if __name__ == '__main__':
    unittest.main()
