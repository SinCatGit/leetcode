import unittest
from maximum_binary_tree_ii import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()

        #     6
        #    / \
        #   1   4
        #      / \
        #     3   2
        t25 = TreeNode(6)
        t21 = TreeNode(1)
        t24 = TreeNode(4)
        t23 = TreeNode(3)
        t26 = TreeNode(2)

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

        root = solution.insertIntoMaxTree(t25, 7)
        self.assertEqual([1, 6, 3, 4, 2, 7], [v for v in dfs(root)])

        root = solution.insertIntoMaxTree(t25, 5)
        self.assertEqual([1, 6, 3, 4, 2, 5], [v for v in dfs(root)])

        #     6
        #    / \
        #   1   4
        #      / \
        #     3   2
        t25 = TreeNode(6)
        t21 = TreeNode(1)
        t24 = TreeNode(4)
        t23 = TreeNode(3)
        t26 = TreeNode(2)

        t25.left = t21
        t25.right = t24

        t24.left = t23
        t24.right = t26
        root = solution.insertIntoMaxTreeV01(t25, 7)
        self.assertEqual([1, 6, 3, 4, 2, 7], [v for v in dfs(root)])

        root = solution.insertIntoMaxTreeV01(t25, 5)
        self.assertEqual([1, 6, 3, 4, 2, 5], [v for v in dfs(root)])


if __name__ == '__main__':
    unittest.main()
