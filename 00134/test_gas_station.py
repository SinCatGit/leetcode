import unittest
from gas_station import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(3, sol.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
        self.assertEqual(-1, sol.canCompleteCircuit([2, 3, 4], [3, 4, 3]))


if __name__ == '__main__':
    unittest.main()
