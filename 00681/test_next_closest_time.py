import unittest
from next_closest_time import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual("19:39", sol.nextClosestTime('19:34'))
        self.assertEqual("22:22", sol.nextClosestTime('23:59'))
        self.assertEqual("15:11", sol.nextClosestTime('11:59'))


if __name__ == '__main__':
    unittest.main()
