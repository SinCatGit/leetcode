import unittest
from basic_calculator import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        self.assertEqual(2, solution.calculate('1 + 1'))
        self.assertEqual(13, solution.calculate(' 12-1 + 2 '))
        self.assertEqual(33, solution.calculate('(1+(14+5+2)-3)+(6+8)'))
        self.assertEqual(2, solution.calculate('10-(1+5+2)'))
        self.assertEqual(1234, solution.calculate('(1234)'))
        self.assertEqual(-1233, solution.calculate('1-(1234)'))


if __name__ == '__main__':
    unittest.main()
