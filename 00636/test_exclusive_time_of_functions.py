import unittest
from exclusive_time_of_functions import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual([3, 4], sol.exclusiveTime(2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]))


if __name__ == '__main__':
    unittest.main()
