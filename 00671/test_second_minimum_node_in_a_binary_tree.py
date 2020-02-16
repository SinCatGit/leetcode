import unittest
from second_minimum_node_in_a_binary_tree import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        #     2
        #    / \
        #   2   5
        #      / \
        #     5   7

        node1 = TreeNode(2)
        node3 = TreeNode(2)
        node2 = TreeNode(5)
        node4 = TreeNode(5)
        node5 = TreeNode(7)

        node1.left = node3
        node1.right = node2
        node2.left = node4
        node2.right = node5

        self.assertEqual(5, sol.findSecondMinimumValue(node1))
        self.assertEqual(5, sol.findSecondMinimumValueV01(node1))

        #    2
        #   / \
        #  2   2
        n2 = TreeNode(2)
        n2_left = TreeNode(2)
        n2_right = TreeNode(2)
        n2.left = n2_left
        n2.right = n2_right

        self.assertEqual(-1, sol.findSecondMinimumValue(n2))
        self.assertEqual(-1, sol.findSecondMinimumValueV01(n2))


if __name__ == '__main__':
    unittest.main()
