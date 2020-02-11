import unittest
from friend_circles import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        self.assertEqual(2, solution.findCircleNum([
            [1, 1, 0],
            [1, 1, 0],
            [0, 0, 1]
        ]))

        self.assertEqual(1, solution.findCircleNum([
            [1, 1, 0],
            [1, 1, 1],
            [0, 1, 1]
        ]))

        self.assertEqual(1, solution.findCircleNum([
            [1, 0, 0, 1],
            [0, 1, 1, 0],
            [0, 1, 1, 1],
            [1, 0, 1, 1]
        ]))


if __name__ == '__main__':
    unittest.main()
