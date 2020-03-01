import unittest
from online_majority_element_in_subarray import MajorityChecker


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = MajorityChecker([1, 1, 2, 2, 1, 1])
        self.assertEqual(1, sol.query(0, 5, 4))
        self.assertEqual(-1, sol.query(0, 3, 3))
        self.assertEqual(2, sol.query(2, 3, 2))

        self.assertEqual(1, sol.queryV01(0, 5, 4))
        self.assertEqual(-1, sol.queryV01(0, 3, 3))
        self.assertEqual(2, sol.queryV01(2, 3, 2))


if __name__ == '__main__':
    unittest.main()
