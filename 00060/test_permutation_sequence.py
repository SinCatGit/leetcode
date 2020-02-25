import unittest
from permutation_sequence import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()

        self.assertEqual('213', sol.getPermutation(3, 3))
        self.assertEqual('2314', sol.getPermutation(4, 9))


if __name__ == '__main__':
    unittest.main()
