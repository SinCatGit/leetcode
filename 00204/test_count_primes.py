import unittest
from count_primes import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()

        self.assertEqual(4, solution.countPrimes(10))
        self.assertEqual(41537, solution.countPrimes(499979))


if __name__ == '__main__':
    unittest.main()
