import unittest
from combinations import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(
            [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]],
            sorted(sol.combine(4, 2))
        )
        self.assertEqual(
            [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3,4]],
            sorted(sol.combineV01(4, 2))
        )


if __name__ == '__main__':
    unittest.main()
