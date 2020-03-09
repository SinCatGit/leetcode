import unittest
from paint_fence import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(6, sol.numWays(3, 2))


if __name__ == '__main__':
    unittest.main()
