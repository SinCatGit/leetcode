import unittest
from reverse_pairs import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(3, sol.reversePairs([5, 2, 6, 1]))
        self.assertEqual(2, sol.reversePairs([1, 3, 2, 3, 1]))


if __name__ == '__main__':
    unittest.main()
