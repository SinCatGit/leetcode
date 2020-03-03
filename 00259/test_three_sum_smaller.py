import unittest
from three_sum_smaller import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(8, sol.threeSumSmaller([1, 0, -1, 0, -2, 2], 0))


if __name__ == '__main__':
    unittest.main()
