import unittest
from meeting_rooms_ii import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()

        self.assertEqual(2, sol.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))


if __name__ == '__main__':
    unittest.main()
