import unittest
from basic_calculator_iii import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        self.assertEqual(-2, solution.calculate('1+3*(2+(1-2)*3)'))
        self.assertEqual(21, solution.calculate('2*(5+5*2)/3+(6/2+8)'))
        self.assertEqual(-12, solution.calculate('(2+6* 3+5- (3*14/7+2)*5)+3'))


if __name__ == '__main__':
    unittest.main()
