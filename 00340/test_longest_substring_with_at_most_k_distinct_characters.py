import unittest
from longest_substring_with_at_most_k_distinct_characters import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(3, sol.lengthOfLongestSubstringKDistinct('eceba', 2))
        self.assertEqual(2, sol.lengthOfLongestSubstringKDistinct('aa', 1))

        self.assertEqual(3, sol.lengthOfLongestSubstringKDistinctV01('eceba', 2))
        self.assertEqual(2, sol.lengthOfLongestSubstringKDistinctV01('aa', 1))


if __name__ == '__main__':
    unittest.main()
