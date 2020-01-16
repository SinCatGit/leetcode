import unittest
from two_num import Solution


class TestSolution(unittest.TestCase):
    def test_TwoSum_Solution(self):
        solution = Solution()
        self.assertEqual([0, 1], solution.twoSum([2, 7, 11, 15], 9))


if __name__ == '__main__':
    unittest.main()
