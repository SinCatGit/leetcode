import unittest
from shortest_word_distance_ii import WordDistance


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
        self.assertEqual(3, sol.shortest('coding', 'practice'))
        self.assertEqual(1, sol.shortest('coding', 'makes'))


if __name__ == '__main__':
    unittest.main()
