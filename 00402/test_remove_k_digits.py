import unittest
from remove_k_digits import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        self.assertEqual('1219', solution.removeKdigits('1432219', 3))
        self.assertEqual('200', solution.removeKdigits('10200', 1))
        self.assertEqual('0', solution.removeKdigits('10', 3))


if __name__ == '__main__':
    unittest.main()
