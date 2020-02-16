import unittest
from minimum_distance_between_bst_nodes import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()

        #       5
        #     /   \
        #   3      7
        #  / \
        # 1   4

        node1 = TreeNode(5)
        node3 = TreeNode(3)
        node2 = TreeNode(7)
        node4 = TreeNode(1)
        node5 = TreeNode(4)

        node1.left = node3
        node1.right = node2
        node3.left = node4
        node3.right = node5

        self.assertEqual(1, sol.minDiffInBST(node1))


if __name__ == '__main__':
    unittest.main()
