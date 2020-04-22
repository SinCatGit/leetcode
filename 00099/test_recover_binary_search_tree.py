import unittest
from recover_binary_search_tree import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        node1 = TreeNode(1)
        node3 = TreeNode(3)
        node2 = TreeNode(2)
        node1.left = node3
        node3.right = node2
        sol.recoverTree(node1)
        self.assertEqual([3, 1], [node1.val, node3.val])

        node1 = TreeNode(1)
        node3 = TreeNode(3)
        node2 = TreeNode(2)
        node1.left = node3
        node3.right = node2
        sol.recoverTreeV01(node1)
        self.assertEqual([3, 1], [node1.val, node3.val])


if __name__ == '__main__':
    unittest.main()
