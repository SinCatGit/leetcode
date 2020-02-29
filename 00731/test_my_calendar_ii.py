import unittest
from my_calendar_ii import MyCalendarTwo


class TestSolution(unittest.TestCase):
    def test_TwoSum_Solution(self):
        sol = MyCalendarTwo()
        self.assertTrue(sol.book(10, 20))
        self.assertTrue(sol.book(50, 60))
        self.assertTrue(sol.book(10, 40))
        self.assertFalse(sol.book(5, 15))
        self.assertTrue(sol.book(5, 10))
        self.assertTrue(sol.book(25, 55))

        sol = MyCalendarTwo()
        self.assertTrue(sol.book(97, 100))
        self.assertTrue(sol.book(51, 65))
        self.assertTrue(sol.book(27, 46))
        self.assertTrue(sol.book(90, 100))
        self.assertTrue(sol.book(20, 32))
        self.assertFalse(sol.book(15, 28))
        self.assertTrue(sol.book(60, 73))
        self.assertTrue(sol.book(77, 91))
        self.assertTrue(sol.book(67, 85))
        self.assertFalse(sol.book(58, 72))
        self.assertFalse(sol.book(74, 93))
        self.assertFalse(sol.book(73, 83))


if __name__ == '__main__':
    unittest.main()
