import unittest
from range_sum_query_2d_mutable import NumMatrix, NumMatrixV01


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = NumMatrix([
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5]
        ])
        self.assertEqual(8, sol.sumRegion(2, 1, 4, 3))
        sol.update(3, 2, 2)
        self.assertEqual(10, sol.sumRegion(2, 1, 4, 3))

        sol = NumMatrixV01([
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5]
        ])
        self.assertEqual(8, sol.sumRegion(2, 1, 4, 3))
        sol.update(3, 2, 2)
        self.assertEqual(10, sol.sumRegion(2, 1, 4, 3))


if __name__ == '__main__':
    unittest.main()
