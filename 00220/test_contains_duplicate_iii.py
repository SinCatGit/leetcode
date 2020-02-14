import unittest
from contains_duplicate_iii import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertTrue(sol.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))
        self.assertTrue(sol.containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2))
        self.assertFalse(sol.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))

        self.assertTrue(sol.containsNearbyAlmostDuplicateV01([1, 2, 3, 1], 3, 0))
        self.assertTrue(sol.containsNearbyAlmostDuplicateV01([1, 0, 1, 1], 1, 2))
        self.assertFalse(sol.containsNearbyAlmostDuplicateV01([1, 5, 9, 1, 5, 9], 2, 3))


if __name__ == '__main__':
    unittest.main()
