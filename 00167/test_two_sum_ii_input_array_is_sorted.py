import unittest
from two_sum_ii_input_array_is_sorted import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()

        self.assertEqual([1, 2], sol.twoSum([2, 7, 11, 15], 9))


if __name__ == '__main__':
    unittest.main()
