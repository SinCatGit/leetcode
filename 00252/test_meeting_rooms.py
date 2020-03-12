import unittest
from meeting_rooms import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()

        self.assertFalse(sol.canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
        self.assertTrue(sol.canAttendMeetings([[7, 10], [2, 4]]))

        self.assertFalse(sol.canAttendMeetingsV01([[0, 30], [5, 10], [15, 20]]))
        self.assertTrue(sol.canAttendMeetingsV01([[7, 10], [2, 4]]))


if __name__ == '__main__':
    unittest.main()
