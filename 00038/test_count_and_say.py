import unittest
from count_and_say import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual('111221', sol.countAndSay(5))
        self.assertEqual('111221', sol.countAndSayV01(5))


if __name__ == '__main__':
    unittest.main()
