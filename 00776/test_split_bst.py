import unittest
from split_bst import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()

        #
        #      4
        #     /  \
        #   2     6
        #  / \   / \
        # 1   3 5   7

        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node5 = TreeNode(5)
        node6 = TreeNode(6)
        node7 = TreeNode(7)

        node4.left = node2
        node4.right = node6
        node2.left = node1
        node2.right = node3
        node6.left = node5
        node6.right = node7

        little, greater = sol.splitBST(node4, 2)

        def dfs(r):
            if r.left:
                yield from dfs(r.left)
            yield r.val
            if r.right:
                yield from dfs(r.right)
        little = dfs(little)
        greater = dfs(greater)
        self.assertEqual(1, next(little))
        self.assertEqual(2, next(little))

        self.assertEqual(3, next(greater))
        self.assertEqual(4, next(greater))
        self.assertEqual(5, next(greater))
        self.assertEqual(6, next(greater))
        self.assertEqual(7, next(greater))


if __name__ == '__main__':
    unittest.main()
