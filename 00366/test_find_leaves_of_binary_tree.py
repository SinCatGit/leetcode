import unittest
from find_leaves_of_binary_tree import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        root = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node5 = TreeNode(5)

        root.left = node2
        root.right = node3

        node2.left = node4
        node2.right = node5

        self.assertEqual([[4, 5, 3], [2], [1]], sol.findLeaves(root))


if __name__ == '__main__':
    unittest.main()
