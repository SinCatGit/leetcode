import unittest
from my_calendar_iii import MyCalendarThree


class TestSolution(unittest.TestCase):
    def test_TwoSum_Solution(self):
        sol = MyCalendarThree()
        # ["MyCalendarThree", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book"]
        # [[], [24, 40], [43, 50], [27, 43], [5, 21], [30, 40], [14, 29], [3, 19], [3, 14], [25, 39], [6, 19]]
        self.assertEqual(1, sol.book(24, 40))
        self.assertEqual(1, sol.book(43, 50))
        self.assertEqual(2, sol.book(27, 43))
        self.assertEqual(2, sol.book(5, 21))
        self.assertEqual(3, sol.book(30, 40))
        self.assertEqual(3, sol.book(14, 29))
        self.assertEqual(3, sol.book(3, 19))
        self.assertEqual(3, sol.book(3, 14))
        self.assertEqual(4, sol.book(25, 39))
        self.assertEqual(4, sol.book(6, 19))


if __name__ == '__main__':
    unittest.main()
