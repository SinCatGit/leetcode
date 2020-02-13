import unittest
from decode_ways import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(2, sol.numDecodings('12'))
        self.assertEqual(1, sol.numDecodings('102'))
        self.assertEqual(3, sol.numDecodings('226'))
        self.assertEqual(0, sol.numDecodings('012'))
        self.assertEqual(0, sol.numDecodings(''))
        self.assertEqual(0, sol.numDecodings('0'))


if __name__ == '__main__':
    unittest.main()
