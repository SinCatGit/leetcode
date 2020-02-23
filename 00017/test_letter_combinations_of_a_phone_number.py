import unittest
from letter_combinations_of_a_phone_number import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(
            ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'],
            sorted(sol.letterCombinations('23'))
        )
        self.assertEqual(
            ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'],
            sorted(sol.letterCombinationsV01('23'))
        )


if __name__ == '__main__':
    unittest.main()
