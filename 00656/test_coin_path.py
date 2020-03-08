import unittest
from coin_path import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual([1, 3, 5], sol.cheapestJump([1, 2, 4, -1, 2], 2))
        self.assertEqual([], sol.cheapestJump([1, 2, 4, -1, 2], 1))


if __name__ == '__main__':
    unittest.main()
