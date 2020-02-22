import unittest
from remove_duplicate_letters import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        self.assertEqual('abc', solution.removeDuplicateLetters('bcabc'))
        self.assertEqual('acdb', solution.removeDuplicateLetters('cbacdcbc'))


if __name__ == '__main__':
    unittest.main()
