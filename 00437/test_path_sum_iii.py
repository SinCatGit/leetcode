import unittest
from path_sum_iii import Solution, TreeNode


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

        #      2
        #     / \
        #    7   4
        #   /   / \
        #  1   3   6
        t35 = TreeNode(2)
        t31 = TreeNode(1)
        t37 = TreeNode(7)
        t34 = TreeNode(4)
        t33 = TreeNode(3)
        t36 = TreeNode(6)

        t35.left = t37
        t37.left = t31
        t35.right = t34

        t34.left = t33
        t34.right = t36

        self.assertEqual(2, sol.pathSum(t35, 10))
        self.assertEqual(2, sol.pathSum(t25, 3))
        self.assertEqual(2, sol.pathSum(t35, 7))

        self.assertEqual(2, sol.pathSumV01(t35, 10))
        self.assertEqual(2, sol.pathSumV01(t25, 3))
        self.assertEqual(2, sol.pathSumV01(t35, 7))


if __name__ == '__main__':
    unittest.main()
