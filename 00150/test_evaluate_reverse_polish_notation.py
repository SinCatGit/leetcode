import unittest
from evaluate_reverse_polish_notation import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        self.assertEqual(9, solution.evalRPN(['2', '1', '+', '3', '*']))
        self.assertEqual(6, solution.evalRPN(['4', '13', '5', '/', '+']))
        self.assertEqual(22, solution.evalRPN(['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']))


if __name__ == '__main__':
    unittest.main()
