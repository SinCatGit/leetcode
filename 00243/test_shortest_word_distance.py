import unittest
from shortest_word_distance import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(3, sol.shortestDistance(
            ['practice', 'makes', 'perfect', 'coding', 'makes'], 'coding', 'practice'
        ))
        self.assertEqual(1, sol.shortestDistance(
            ['practice', 'makes', 'perfect', 'coding', 'makes'], 'makes', 'coding'
        ))
        self.assertEqual(2, sol.shortestDistance(
            ['practice', 'makes', 'makes', 'perfect', 'world', 'coding', 'coding', 'hello', 'makes'], 'makes', 'coding'
        ))

        self.assertEqual(3, sol.shortestDistanceV01(
            ['practice', 'makes', 'perfect', 'coding', 'makes'], 'coding', 'practice'
        ))
        self.assertEqual(1, sol.shortestDistanceV01(
            ['practice', 'makes', 'perfect', 'coding', 'makes'], 'makes', 'coding'
        ))
        self.assertEqual(2, sol.shortestDistanceV01(
            ['practice', 'makes', 'makes', 'perfect', 'world', 'coding', 'coding', 'hello', 'makes'], 'makes', 'coding'
        ))


if __name__ == '__main__':
    unittest.main()
