import unittest
from minimum_window_substring import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        self.assertEqual('BANC', solution.minWindow('ADOBECODEBANC', 'ABC'))


if __name__ == '__main__':
    unittest.main()
