import unittest
from contains_duplicate_ii import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertTrue(sol.containsNearbyDuplicate([1, 2, 3, 1], 3))
        self.assertTrue(sol.containsNearbyDuplicate([1, 0, 1, 1], 1))
        self.assertFalse(sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))

        self.assertTrue(sol.containsNearbyDuplicateV01([1, 2, 3, 1], 3))
        self.assertTrue(sol.containsNearbyDuplicateV01([1, 0, 1, 1], 1))
        self.assertFalse(sol.containsNearbyDuplicateV01([1, 2, 3, 1, 2, 3], 2))


if __name__ == '__main__':
    unittest.main()
