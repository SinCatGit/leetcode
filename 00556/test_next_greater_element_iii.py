import unittest
from next_greater_element_iii import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(21, sol.nextGreaterElement(12))
        self.assertEqual(323145, sol.nextGreaterElement(321543))
        self.assertEqual(-1, sol.nextGreaterElement(21))
        self.assertEqual(-1, sol.nextGreaterElement(54321))
        self.assertEqual(-1, sol.nextGreaterElement(1))
        self.assertEqual(9199999999, sol.nextGreaterElement(1999999999))


if __name__ == '__main__':
    unittest.main()
