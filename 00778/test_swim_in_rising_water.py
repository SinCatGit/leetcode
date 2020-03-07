import unittest
from swim_in_rising_water import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(
            16, sol.swimInWater([
                [0, 1, 2, 3, 4],
                [24, 23, 22, 21, 5],
                [12, 13, 14, 15, 16],
                [11, 17, 18, 19, 20],
                [10, 9, 8, 7, 6]
            ]))


if __name__ == '__main__':
    unittest.main()
