import unittest
from count_of_smaller_numbers_after_self import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual([2, 1, 1, 0], sol.countSmaller([5, 2, 6, 1]))


if __name__ == '__main__':
    unittest.main()
