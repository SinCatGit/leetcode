import unittest
from sparse_matrix_multiplication import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual([[7, 0, 0], [-7, 0, 3]], sol.multiply(
            [[1, 0, 0], [-1, 0, 3]],
            [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
        ))


if __name__ == '__main__':
    unittest.main()
