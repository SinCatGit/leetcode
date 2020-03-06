import unittest
from number_of_digit_one import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(6, sol.countDigitOne(13))
        self.assertEqual(25, sol.countDigitOne(103))


if __name__ == '__main__':
    unittest.main()
