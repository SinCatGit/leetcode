import unittest
from basic_calculator_ii import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        self.assertEqual(7, solution.calculate('3+2*2'))
        self.assertEqual(1, solution.calculate(' 3/2'))
        self.assertEqual(5, solution.calculate(' 3+5 / 2'))
        self.assertEqual(-4, solution.calculate(' 3-5 / 2*2-3'))


if __name__ == '__main__':
    unittest.main()
