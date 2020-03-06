import unittest
from set_matrix_zeroes import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        matrix = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
        sol.setZeroes(matrix)
        self.assertEqual([[1, 0, 1], [0, 0, 0], [1, 0, 1]], matrix)

        matrix = [
            [0, 1, 2, 0],
            [3, 4, 5, 2],
            [1, 3, 1, 5]
        ]
        sol.setZeroes(matrix)
        self.assertEqual([[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]], matrix)


if __name__ == '__main__':
    unittest.main()
