import unittest
from rectangle_area_ii import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(6, sol.rectangleArea([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]))
        self.assertEqual(49, sol.rectangleArea([[0,0,1000000000,1000000000]]))

        self.assertEqual(6, sol.rectangleAreaV01([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]))
        self.assertEqual(49, sol.rectangleAreaV01([[0,0,1000000000,1000000000]]))


if __name__ == '__main__':
    unittest.main()
