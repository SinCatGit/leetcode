import unittest
from find_bottom_left_tree_value import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()

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

        self.assertEqual(3, sol.findBottomLeftValue(t25))


if __name__ == '__main__':
    unittest.main()
