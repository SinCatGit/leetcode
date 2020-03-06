import unittest
from parse_lisp_expression import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(3, sol.evaluate('(add 1 2)'))
        self.assertEqual(15, sol.evaluate('(mult 3 (add 2 3))'))
        self.assertEqual(10, sol.evaluate('(let x 2 (mult x 5))'))
        self.assertEqual(2, sol.evaluate('(let x 3 x 2 x)'))
        self.assertEqual(5, sol.evaluate('(let x 1 y 2 x (add x y) (add x y))'))
        self.assertEqual(6, sol.evaluate('(let x 2 (add (let x 3 (let x 4 x)) x))'))
        self.assertEqual(4, sol.evaluate('(let a1 3 b2 (add a1 1) b2)'))


if __name__ == '__main__':
    unittest.main()
