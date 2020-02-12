import unittest
from reorganize_string import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual('aba', sol.reorganizeString('aab'))
        self.assertEqual('', sol.reorganizeString('aaab'))
        self.assertEqual('a', sol.reorganizeString('a'))

        self.assertEqual('aba', sol.reorganizeStringV01('aab'))
        self.assertEqual('', sol.reorganizeStringV01('aaab'))
        self.assertEqual('a', sol.reorganizeStringV01('a'))


if __name__ == '__main__':
    unittest.main()
