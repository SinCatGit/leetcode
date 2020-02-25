import unittest
from palindrome_permutation_ii import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()

        self.assertEqual(['abba', 'baab'], sorted(sol.generatePalindromes('aabb')))
        self.assertEqual(['abcba', 'bacab'], sorted(sol.generatePalindromes('aacbb')))
        self.assertEqual([], sorted(sol.generatePalindromes('abc')))


if __name__ == '__main__':
    unittest.main()
