import unittest
from two_sum_iii_data_structure_design import TwoSum


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = TwoSum()
        sol.add(3)
        sol.add(5)
        sol.add(3)
        sol.add(7)
        sol.add(9)
        self.assertTrue(sol.find(8))
        self.assertFalse(sol.find(18))


if __name__ == '__main__':
    unittest.main()
