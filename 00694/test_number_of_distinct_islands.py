import unittest
from number_of_distinct_islands import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        self.assertEqual(
            1,
            solution.numberofDistinctIslands(
                [
                    ['1', '1', '0', '0', '0'],
                    ['1', '1', '0', '0', '0'],
                    ['0', '0', '0', '1', '1'],
                    ['0', '0', '0', '1', '1']
                ]
            )
        )

        self.assertEqual(
            3,
            solution.numberofDistinctIslands(
                [
                    ['1', '1', '0', '0', '1'],
                    ['1', '0', '0', '0', '0'],
                    ['1', '1', '0', '0', '1'],
                    ['0', '1', '0', '1', '1']
                ]
            )
        )


if __name__ == '__main__':
    unittest.main()
