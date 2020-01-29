import unittest
from top_k_frequent_words import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        self.assertEqual(["i", "love"], solution.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
        self.assertEqual(
            ["the", "is", "sunny", "day"],
            solution.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))


if __name__ == '__main__':
    unittest.main()
