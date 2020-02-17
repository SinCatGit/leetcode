import unittest
from search_in_a_binary_search_tree import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()

        # Given the tree:
        #         4
        #        / \
        #       2   7
        #      / \
        #     1   3
        # And the value to insert: 5
        # You can return this binary search tree:
        #
        #          4
        #        /   \
        #       2     7
        #      / \   /
        #     1   3 5
        node4 = TreeNode(4)
        node2 = TreeNode(2)
        node1 = TreeNode(1)
        node3 = TreeNode(3)
        node7 = TreeNode(7)

        node4.left = node2
        node4.right = node7

        node2.left = node1
        node2.right = node3

        insert_tree = sol.searchBST(node4, 2)

        def dfs(r):
            if r.left:
                yield from dfs(r.left)
            yield r.val
            if r.right:
                yield from dfs(r.right)
        insert_tree = dfs(insert_tree)
        self.assertEqual([1, 2, 3], [item for item in insert_tree])


if __name__ == '__main__':
    unittest.main()
