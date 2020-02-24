import unittest
from permutations import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
            sorted(sol.permute([1, 2, 3]))
        )

        self.assertEqual(
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
            sorted(sol.permuteV01([1, 2, 3]))
        )


if __name__ == '__main__':
    unittest.main()
