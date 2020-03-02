import unittest
from maximum_number_of_events_that_can_be_attended import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(3, sol.maxEvents([[1, 2], [2, 3], [3, 4]]))
        self.assertEqual(4, sol.maxEvents([[1, 2], [2, 3], [3, 4], [1, 2]]))
        self.assertEqual(7, sol.maxEvents([[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]]))


if __name__ == '__main__':
    unittest.main()
