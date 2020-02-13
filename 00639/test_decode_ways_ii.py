import unittest
from decode_ways_ii import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(9, sol.numDecodings('*'))
        self.assertEqual(18, sol.numDecodings('1*'))
        self.assertEqual(404, sol.numDecodings('*1*1*0'))


if __name__ == '__main__':
    unittest.main()
