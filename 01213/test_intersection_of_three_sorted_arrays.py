import unittest
from intersection_of_three_sorted_arrays import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual([1, 5], sol.arraysIntersection([1, 2, 3, 4, 5], [1, 2, 5, 7, 9], [1, 3, 4, 5, 8]))


if __name__ == '__main__':
    unittest.main()
