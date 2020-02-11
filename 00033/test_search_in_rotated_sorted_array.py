import unittest
from search_in_rotated_sorted_array import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(4, sol.search(
            [4, 5, 6, 7, 0, 1, 2], 0
        ))
        self.assertEqual(-1, sol.search(
            [4, 5, 6, 7, 0, 1, 2], 3
        ))
        self.assertEqual(5, sol.search(
            [4, 5, 6, 7, 8, 1, 2], 1
        ))
        self.assertEqual(0, sol.search(
            [4, 5, 6, 7, 8, 1, 2], 4
        ))

        self.assertEqual(4, sol.search(
            [7, 8, 1, 2, 4, 5, 6], 4
        ))

        self.assertEqual(0, sol.search(
            [1], 1
        ))


if __name__ == '__main__':
    unittest.main()
