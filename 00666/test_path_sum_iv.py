import unittest
from path_sum_iv import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()

        self.assertEqual(12, sol.pathSum([113, 215, 221]))
        self.assertEqual(12, sol.pathSum([113, 215, 324]))


if __name__ == '__main__':
    unittest.main()
