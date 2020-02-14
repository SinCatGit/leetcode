import unittest
from find_duplicate_subtrees import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        root = TreeNode(1)
        node11 = TreeNode(2)
        node12 = TreeNode(3)
        node21 = TreeNode(4)
        node22 = TreeNode(2)
        node23 = TreeNode(4)
        node31 = TreeNode(4)
        root.left = node11
        root.right = node12
        node11.left = node21
        node12.left = node22
        node12.right = node23
        node22.left = node31
        result = sol.findDuplicateSubtrees(root)
        result01 = sol.findDuplicateSubtreesV01(root)

        self.assertEqual({id(node11), id(node21)}, set([id(item) for item in result]))
        self.assertEqual({id(node11), id(node21)}, set([id(item) for item in result01]))


if __name__ == '__main__':
    unittest.main()
