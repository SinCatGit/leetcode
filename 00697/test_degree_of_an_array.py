import unittest
from degree_of_an_array import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        self.assertEqual(6, solution.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))
        self.assertEqual(6, solution.findShortestSubArrayV01([1, 2, 2, 3, 1, 4, 2]))


if __name__ == '__main__':
    unittest.main()