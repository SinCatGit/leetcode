import unittest
from pour_water import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual([2, 2, 2, 3, 2, 2, 2], sol.pourWater([2, 1, 1, 2, 1, 2, 2], 4, 3))
        self.assertEqual([2, 3, 3, 4], sol.pourWater([1, 2, 3, 4], 2, 2))
        self.assertEqual([4, 4, 4], sol.pourWater([3, 1, 3], 5, 1))

        self.assertEqual([2, 2, 2, 3, 2, 2, 2], sol.pourWaterV01([2, 1, 1, 2, 1, 2, 2], 4, 3))
        self.assertEqual([2, 3, 3, 4], sol.pourWaterV01([1, 2, 3, 4], 2, 2))
        self.assertEqual([4, 4, 4], sol.pourWaterV01([3, 1, 3], 5, 1))


if __name__ == '__main__':
    unittest.main()
