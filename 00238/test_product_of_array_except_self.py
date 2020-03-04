import unittest
from product_of_array_except_self import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual([24, 12, 8, 6], sol.productExceptSelf([1, 2, 3, 4]))


if __name__ == '__main__':
    unittest.main()
