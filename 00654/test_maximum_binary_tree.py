import unittest
from maximum_binary_tree import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()

        #       6
        #     /   \
        #    3     5
        #     \    /
        #      2  0
        #        \
        #         1

        def dfs(r):
            if r.left:
                yield from dfs(r.left)
            yield r.val
            if r.right:
                yield from dfs(r.right)
        root = solution.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
        self.assertEqual([3, 2, 1, 6, 0, 5], [v for v in dfs(root)])

        root = solution.constructMaximumBinaryTreeV01([3, 2, 1, 6, 0, 5])
        self.assertEqual([3, 2, 1, 6, 0, 5], [v for v in dfs(root)])


if __name__ == '__main__':
    unittest.main()
