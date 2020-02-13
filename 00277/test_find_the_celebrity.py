import unittest
from find_the_celebrity import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution([[1, 1, 0], [0, 1, 0], [1, 1, 1]])
        self.assertEqual(1, sol.findCelebrity(3))

        sol = Solution([[1, 0, 1], [1, 1, 0], [0, 1, 1]])
        self.assertEqual(-1, sol.findCelebrity(3))

        sol = Solution([[1, 1, 0], [0, 1, 0], [1, 1, 1]])
        self.assertEqual(1, sol.findCelebrityV01(3))

        sol = Solution([[1, 0, 1], [1, 1, 0], [0, 1, 1]])
        self.assertEqual(-1, sol.findCelebrityV01(3))


if __name__ == '__main__':
    unittest.main()
