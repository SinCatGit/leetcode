import unittest
from merge_two_binary_trees import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()

        #
        # Input:
        #     Tree 1                     Tree 2
        #           1                         2
        #          / |                       / \
        #         3   2                     1   3
        #        /                           |   \
        #       5                             4   7

        # Output:
        # Merged tree:
        #          3
        #         / \
        #        4   5
        #       / |   \
        #      5   4   7

        tree1 = TreeNode(1)
        t13 = TreeNode(3)
        t12 = TreeNode(2)
        t15 = TreeNode(5)

        tree1.left = t13
        tree1.right = t12
        t13.left = t15

        tree2 = TreeNode(2)
        t21 = TreeNode(1)
        t23 = TreeNode(3)
        t24 = TreeNode(4)
        t27 = TreeNode(7)

        tree2.left = t21
        tree2.right = t23
        t21.right = t24
        t23.right = t27

        merge_tree = sol.mergeTrees(tree1, tree2)

        def dfs(r):
            if r.left:
                yield from dfs(r.left)
            yield r.val
            if r.right:
                yield from dfs(r.right)
        merge_tree = dfs(merge_tree)
        self.assertEqual([5, 4, 4, 3, 5, 7], [item for item in merge_tree])


if __name__ == '__main__':
    unittest.main()
