import unittest
from number_of_squareful_arrays import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()

        self.assertEqual(2, sol.numSquarefulPerms([1, 17, 8]))
        self.assertEqual(1, sol.numSquarefulPerms([2, 2, 2]))


if __name__ == '__main__':
    unittest.main()
