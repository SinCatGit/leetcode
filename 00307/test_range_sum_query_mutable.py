import unittest
from range_sum_query_mutable import NumArray


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = NumArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(15, sol.sumRange(6, 7))
        sol.update(6, 5)
        self.assertEqual(13, sol.sumRange(6, 7))


if __name__ == '__main__':
    unittest.main()
