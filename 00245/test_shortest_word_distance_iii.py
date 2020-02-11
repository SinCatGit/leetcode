import unittest
from shortest_word_distance_iii import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(3, sol.shortestDistance(
            ['practice', 'makes', 'perfect', 'coding', 'makes'], 'coding', 'practice'
        ))
        self.assertEqual(3, sol.shortestDistance(
            ['practice', 'makes', 'perfect', 'coding', 'makes'], 'makes', 'makes'
        ))


if __name__ == '__main__':
    unittest.main()
