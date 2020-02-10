import unittest
from number_of_connected_components_in_an_undirected_graph import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        self.assertEqual(2, solution.countComponents(5, [[0, 1], [1, 2], [3, 4]]))


if __name__ == '__main__':
    unittest.main()
