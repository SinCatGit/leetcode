import unittest
from longest_univalue_path import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        node1 = TreeNode(5)
        node2 = TreeNode(4)
        node3 = TreeNode(5)
        node4 = TreeNode(1)
        node5 = TreeNode(1)
        node6 = TreeNode(5)
        node1.left = node2
        node1.right = node3
        node2.left = node4
        node2.right = node5
        node3.right = node6
        solution = Solution()
        self.assertEqual(2, solution.longestUnivaluePath(node1))


if __name__ == '__main__':
    unittest.main()
