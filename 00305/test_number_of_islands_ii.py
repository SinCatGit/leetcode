import unittest
from number_of_islands_ii import Solution, Point


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        self.assertEqual(
            [1, 1, 2, 2],
            solution.numIslands2(4, 5, [Point(1, 1), Point(0, 1), Point(3, 3), Point(3, 4)])
        )

        self.assertEqual(
            [1, 1, 2, 2],
            solution.numIslands2(3, 3, [Point(0, 0), Point(0, 1), Point(2, 2), Point(2, 2)])
        )

        self.assertEqual(
            [1, 1, 2, 2],
            solution.numIslands2V01(4, 5, [Point(1, 1), Point(0, 1), Point(3, 3), Point(3, 4)])
        )

        self.assertEqual(
            [1, 1, 2, 2],
            solution.numIslands2V01(3, 3, [Point(0, 0), Point(0, 1), Point(2, 2), Point(2, 2)])
        )


if __name__ == '__main__':
    unittest.main()
