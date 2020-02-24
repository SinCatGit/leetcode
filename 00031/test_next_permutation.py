import unittest
from next_permutation import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()

        nums = [5, 4, 3, 6, 4, 3, 2]
        sol.nextPermutation(nums)
        self.assertEqual([5, 4, 4, 2, 3, 3, 6], nums)

        nums = [5, 4, 3, 2]
        sol.nextPermutation(nums)
        self.assertEqual([2, 3, 4, 5], nums)

        nums = [1, 1, 5]
        sol.nextPermutation(nums)
        self.assertEqual([1, 5, 1], nums)


if __name__ == '__main__':
    unittest.main()
