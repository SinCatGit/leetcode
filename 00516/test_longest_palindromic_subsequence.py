import unittest
from longest_palindromic_subsequence import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        self.assertEqual(4, solution.longestPalindromeSubseq('bbbab'))
        self.assertEqual(2, solution.longestPalindromeSubseq('cbbd'))
        self.assertEqual(5, solution.longestPalindromeSubseq('agbdba'))

        self.assertEqual(4, solution.longestPalindromeSubseqV01('bbbab'))
        self.assertEqual(2, solution.longestPalindromeSubseqV01('cbbd'))
        self.assertEqual(5, solution.longestPalindromeSubseqV01('agbdba'))

        self.assertEqual(4, solution.longestPalindromeSubseqV02('bbbab'))
        self.assertEqual(2, solution.longestPalindromeSubseqV02('cbbd'))
        self.assertEqual(5, solution.longestPalindromeSubseqV02('agbdba'))


if __name__ == '__main__':
    unittest.main()
