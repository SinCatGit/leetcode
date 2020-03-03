import unittest
from remove_duplicates_from_sorted_array_ii import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        nums = [1, 1, 1, 2, 2, 3]
        self.assertEqual(5, sol.removeDuplicates(nums))
        self.assertEqual([1, 1, 2, 2, 3], nums[:5])

        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        self.assertEqual(7, sol.removeDuplicates(nums))
        self.assertEqual([0, 0, 1, 1, 2, 3, 3], nums[:7])


if __name__ == '__main__':
    unittest.main()
