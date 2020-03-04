import unittest
from trapping_rain_water import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        nums = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        self.assertEqual(6, sol.trap(nums))
        self.assertEqual(6, sol.trapV01(nums))
        self.assertEqual(6, sol.trapV02(nums))


if __name__ == '__main__':
    unittest.main()
