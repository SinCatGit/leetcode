import unittest
from smallest_range_covering_elements_from_k_lists import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual([20, 24], sol.smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
        self.assertEqual([1, 1], sol.smallestRange([[1, 2, 3], [1, 2, 3]]))
        self.assertEqual([1, 7], sol.smallestRange([[1], [2], [3], [4], [5], [6], [7]]))
        self.assertEqual([1, 7], sol.smallestRange([[1], [2], [3], [5], [4], [6], [7]]))
        self.assertEqual([1, 8], sol.smallestRange([[1], [2], [3], [5], [4], [6], [7], [8]]))

        self.assertEqual([20, 24], sol.smallestRangeV01([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
        self.assertEqual([1, 1], sol.smallestRangeV01([[1, 2, 3], [1, 2, 3]]))
        self.assertEqual([1, 7], sol.smallestRangeV01([[1], [2], [3], [4], [5], [6], [7]]))
        self.assertEqual([1, 7], sol.smallestRangeV01([[1], [2], [3], [5], [4], [6], [7]]))
        self.assertEqual([1, 8], sol.smallestRangeV01([[1], [2], [3], [5], [4], [6], [7], [8]]))


if __name__ == '__main__':
    unittest.main()
