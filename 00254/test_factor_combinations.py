import unittest
from factor_combinations import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()

        self.assertEqual([[2, 6], [3, 4], [2, 2, 3]], sol.getFactors(12))
        self.assertEqual([], sol.getFactors(37))
        self.assertEqual(
            [
                [2, 16],
                [4, 8],
                [2, 2, 8],
                [2, 4, 4],
                [2, 2, 2, 4],
                [2, 2, 2, 2, 2]
            ], sol.getFactors(32))

        self.assertEqual([[2, 6], [2, 2, 3], [3, 4]], sol.getFactorsV01(12))
        self.assertEqual([], sol.getFactorsV01(37))
        self.assertEqual(
            [
                [2, 16],
                [2, 2, 8],
                [2, 2, 2, 4],
                [2, 2, 2, 2, 2],
                [2, 4, 4],
                [4, 8]
            ], sol.getFactorsV01(32))


if __name__ == '__main__':
    unittest.main()
