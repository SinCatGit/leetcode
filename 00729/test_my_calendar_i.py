import unittest
from my_calendar_i import MyCalendar


class TestSolution(unittest.TestCase):
    def test_TwoSum_Solution(self):
        sol = MyCalendar()
        self.assertTrue(sol.book(10, 15))
        self.assertTrue(sol.book(20, 25))
        self.assertTrue(sol.book(15, 20))
        self.assertFalse(sol.book(5, 20))


if __name__ == '__main__':
    unittest.main()
