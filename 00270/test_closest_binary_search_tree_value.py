import unittest
from closest_binary_search_tree_value import Solution, TreeNode


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

        self.assertEqual(4, sol.closestValue(node4, 4.5))
        self.assertEqual(4, sol.closestValueV01(node4, 4.5))


if __name__ == '__main__':
    unittest.main()
