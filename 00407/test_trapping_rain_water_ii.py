import unittest
from trapping_rain_water_ii import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        nums = [
            [1, 4, 3, 1, 3, 2],
            [3, 2, 1, 3, 2, 4],
            [2, 3, 3, 2, 3, 1]
        ]
        self.assertEqual(4, sol.trapRainWater(nums))
        nums = [
            [12, 13, 1, 12],
            [13, 4, 13, 12],
            [13, 8, 10, 12],
            [12, 13, 12, 12],
            [13, 13, 13, 13]
        ]
        self.assertEqual(14, sol.trapRainWater(nums))


if __name__ == '__main__':
    unittest.main()
