import unittest
from binary_tree_longest_consecutive_sequence import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        root = TreeNode(1)
        node3 = TreeNode(3)
        node2 = TreeNode(2)
        node4 = TreeNode(4)
        node5 = TreeNode(5)

        root.right = node3
        node3.left = node2
        node3.right = node4
        node4.right = node5

        self.assertEqual(3, sol.longestConsecutive(root))


if __name__ == '__main__':
    unittest.main()
