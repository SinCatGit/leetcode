import unittest
from prime_number_of_set_bits_in_binary_representation import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        self.assertEqual(4, solution.countPrimeSetBits(6, 10))
        self.assertEqual(5, solution.countPrimeSetBits(10, 15))

        self.assertEqual(4, solution.countPrimeSetBitsV01(6, 10))
        self.assertEqual(5, solution.countPrimeSetBitsV01(10, 15))


if __name__ == '__main__':
    unittest.main()
