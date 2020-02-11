import unittest
from search_in_rotated_sorted_array_ii import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertFalse(sol.search([2, 5, 6, 0, 0, 1, 2], 3))
        self.assertTrue(sol.search([2, 5, 6, 0, 0, 1, 2], 0))
        self.assertTrue(sol.search([3, 4, 3, 3, 3, 3, 3], 4))


if __name__ == '__main__':
    unittest.main()
