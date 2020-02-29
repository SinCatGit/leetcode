
class Node:
    def __init__(self, l, r, count):
        self.l = l
        self.r = r
        self.m = -1
        self.count = count
        self.left = None
        self.right = None


class MyCalendarThree:
    def __init__(self):
        self.root = Node(float('-inf'), float('inf'), 0)
        self.cnt = 0

    def book(self, start: int, end: int) -> int:
        """
        [732. My Calendar III](https://leetcode.com/problems/my-calendar-iii/)

        Implement a MyCalendarThree class to store your events. A new event can always be added.

        Your class will have one method, book(int start, int end). Formally, this represents a
        booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

        A K-booking happens when K events have some non-empty intersection (ie., there is some time
        that is common to all K events.)

        For each call to the method MyCalendar.book, return an integer K representing the largest integer
        such that there exists a K-booking in the calendar.

        Your class will be called like this: MyCalendarThree cal = new MyCalendarThree();
        MyCalendarThree.book(start, end)

        **Example 1:**

        ```
        MyCalendarThree();
        MyCalendarThree.book(10, 20); // returns 1
        MyCalendarThree.book(50, 60); // returns 1
        MyCalendarThree.book(10, 40); // returns 2
        MyCalendarThree.book(5, 15); // returns 3
        MyCalendarThree.book(5, 10); // returns 3
        MyCalendarThree.book(25, 55); // returns 3
        Explanation:
        The first two events can be booked and are disjoint, so the maximum K-booking is a 1-booking.
        The third event [10, 40) intersects the first event, and the maximum K-booking is a 2-booking.
        The remaining events cause the maximum K-booking to be only a 3-booking.
        Note that the last event locally causes a 2-booking, but the answer is still 3 because
        eg. [10, 20), [10, 40), and [5, 15) are still triple booked.
        ```

        **Note:**

        - The number of calls to MyCalendarThree.book per test case will be at most 400.
        - In calls to MyCalendarThree.book(start, end), start and end are integers in the range [0, 10^9].

        """
        self.add(start, end, self.root)
        return self.cnt

    def add(self, start, end, root):
        if root.m != -1:
            if start >= root.m:
                self.add(start, end, root.right)
            elif end <= root.m:
                self.add(start, end, root.left)
            else:
                self.add(start, root.m, root.left)
                self.add(root.m, end, root.right)
            return

        if start == root.l and end == root.r:
            root.count += 1
            self.cnt = max(self.cnt, root.count)
        elif start == root.l:
            root.m = end
            root.left = Node(start, root.m, root.count+1)
            root.right = Node(root.m, root.right, root.count)
            self.cnt = max(self.cnt, root.count+1)
        elif end == root.r:
            root.m = start
            root.left = Node(root.l, root.m, root.count)
            root.right = Node(root.m, end, root.count+1)
            self.cnt = max(self.cnt, root.count+1)
        else:
            root.m = start
            root.left = Node(root.l, root.m, root.count)
            root.right = Node(root.m, root.r, root.count)
            self.add(start, end, root.right)

