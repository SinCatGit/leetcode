import unittest
from kth_smallest_element_in_a_bst import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        #    5
        #   / \
        #   3  6
        #  /  \ \
        #  2  4  7

        node1 = TreeNode(5)
        node3 = TreeNode(3)
        node2 = TreeNode(6)
        node4 = TreeNode(2)
        node5 = TreeNode(4)
        node6 = TreeNode(7)

        node1.left = node3
        node1.right = node2
        node3.left = node4
        node3.right = node5
        node2.right = node6

        self.assertEqual(2, sol.kthSmallest(node1, 1))
        self.assertEqual(3, sol.kthSmallest(node1, 2))
        self.assertEqual(4, sol.kthSmallest(node1, 3))
        self.assertEqual(7, sol.kthSmallest(node1, 6))


if __name__ == '__main__':
    unittest.main()
