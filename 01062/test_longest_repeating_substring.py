import unittest
from longest_repeating_substring import Solution


class TestSolution(unittest.TestCase):
    def test_longestRepeatingSubstring_Solution(self):
        sol = Solution()
        self.assertEqual(2, sol.longestRepeatingSubstring('abbaba'))
        self.assertEqual(4, sol.longestRepeatingSubstring('aaaaa'))
        self.assertEqual(0, sol.longestRepeatingSubstring('abcd'))
        self.assertEqual(3, sol.longestRepeatingSubstring('aabcaabdaab'))

        self.assertEqual(2, sol.longestRepeatingSubstringV01('abbaba'))
        self.assertEqual(4, sol.longestRepeatingSubstringV01('aaaaa'))
        self.assertEqual(0, sol.longestRepeatingSubstringV01('abcd'))
        self.assertEqual(3, sol.longestRepeatingSubstringV01('aabcaabdaab'))


if __name__ == '__main__':
    unittest.main()
