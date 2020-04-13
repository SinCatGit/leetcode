import unittest
from palindrome_removal import Solution


class TestSolution(unittest.TestCase):
    def test_minimumMoves_Solution(self):
        sol = Solution()
        self.assertEqual(3, sol.minimumMoves([1, 3, 4, 1, 5]))
        self.assertEqual(4, sol.minimumMoves([16, 13, 13, 10, 12]))

        self.assertEqual(3, sol.minimumMovesV01([1, 3, 4, 1, 5]))
        self.assertEqual(4, sol.minimumMovesV01([16, 13, 13, 10, 12]))


if __name__ == '__main__':
    unittest.main()
