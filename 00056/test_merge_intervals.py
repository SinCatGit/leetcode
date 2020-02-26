import unittest
from merge_intervals import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(
            [[1, 6], [8, 10], [15, 18]],
            sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
        )
        self.assertEqual(
            [[1, 5]],
            sol.merge([[1, 4], [4, 5]])
        )


if __name__ == '__main__':
    unittest.main()
