import unittest
from alien_dictionary import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual('zx', sol.alienOrder(['z', 'x']))
        self.assertEqual('yxz', sol.alienOrder(['zy', 'zx']))
        self.assertEqual('wertf', sol.alienOrder(['wrt', 'wrf', 'er', 'ett', 'rftt']))
        self.assertEqual('zyxwvutsrqponmlkjihgfedcba', sol.alienOrder([
            "ze", "yf", "xd", "wd", "vd", "ua", "tt", "sz", "rd", "qd", "pz", "op", "nw", "mt",
            "ln", "ko", "jm", "il", "ho", "gk", "fa", "ed", "dg", "ct", "bb", "ba"
        ]))


if __name__ == '__main__':
    unittest.main()
