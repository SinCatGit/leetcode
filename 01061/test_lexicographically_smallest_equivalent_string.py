import unittest
from lexicographically_smallest_equivalent_string import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()

        self.assertEqual('makkek', sol.smallestEquivalentString('parker', 'morris', 'parser'))
        self.assertEqual('hdld', sol.smallestEquivalentString('hello', 'world', 'hold'))
        self.assertEqual('aauaaaaada', sol.smallestEquivalentString('leetcode', 'programs', 'sourcecode'))


if __name__ == '__main__':
    unittest.main()
