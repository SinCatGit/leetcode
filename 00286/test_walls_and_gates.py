import unittest
from walls_and_gates import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        solution = Solution()
        rooms = [
            [2147483647, -1, 0, 2147483647],
            [2147483647, 2147483647, 2147483647, -1],
            [2147483647, -1, 2147483647, -1],
            [0, -1, 2147483647, 2147483647]
        ]

        res_rooms = [
            [3, -1, 0, 1],
            [2, 2, 1, -1],
            [1, -1, 2, -1],
            [0, -1, 3, 4]
        ]

        solution.wallsAndGates(rooms)
        self.assertEqual(res_rooms, rooms)


if __name__ == '__main__':
    unittest.main()
