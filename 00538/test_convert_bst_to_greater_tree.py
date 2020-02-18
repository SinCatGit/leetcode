import unittest
from convert_bst_to_greater_tree import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()

        #     2
        #    / \
        #   1   4
        #      / \
        #     3   6
        t25 = TreeNode(2)
        t21 = TreeNode(1)
        t24 = TreeNode(4)
        t23 = TreeNode(3)
        t26 = TreeNode(6)

        t25.left = t21
        t25.right = t24

        t24.left = t23
        t24.right = t26

        def dfs(r):
            if r.left:
                yield from dfs(r.left)
            yield r.val
            if r.right:
                yield from dfs(r.right)
        root = solution.convertBST(t25)
        self.assertEqual([16, 15, 13, 10, 6], [v for v in dfs(root)])


if __name__ == '__main__':
    unittest.main()
