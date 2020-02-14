import unittest
from contains_duplicate import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertTrue(sol.containsDuplicate([1, 2, 3, 1]))
        self.assertFalse(sol.containsDuplicate([1, 2, 3]))


if __name__ == '__main__':
    unittest.main()
