import unittest
from insert_interval import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(
            [[1, 5], [6, 9]],
            sol.insert([[1, 3], [6, 9]], [2, 5])
        )
        self.assertEqual(
            [[1, 2], [3, 10],[12, 16]],
            sol.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
        )


if __name__ == '__main__':
    unittest.main()
