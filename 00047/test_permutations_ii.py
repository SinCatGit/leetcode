import unittest
from permutations_ii import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(
            [[1, 1, 2], [1, 2, 1], [2, 1, 1]],
            sorted(sol.permuteUnique([1, 1, 2]))
        )

        self.assertEqual(
            [[1, 1, 2], [1, 2, 1], [2, 1, 1]],
            sorted(sol.permuteUniqueV01([1, 1, 2]))
        )


if __name__ == '__main__':
    unittest.main()
