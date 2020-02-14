import unittest
from construct_string_from_binary_tree import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        root1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        root1.left = node2
        root1.right = node3
        node2.left = node4

        self.assertEqual('1(2(4))(3)', sol.tree2str(root1))

        root2 = TreeNode(1)
        node22 = TreeNode(2)
        node23 = TreeNode(3)
        node24 = TreeNode(4)
        root2.left = node22
        root2.right = node23
        node22.right = node24
        self.assertEqual('1(2()(4))(3)', sol.tree2str(root2))


if __name__ == '__main__':
    unittest.main()
