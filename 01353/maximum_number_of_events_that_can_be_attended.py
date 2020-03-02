from typing import List
from collections import defaultdict
from bisect import bisect_left as bl
from bisect import bisect_right as br
from random import randint


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        [1353. Maximum Number of Events That Can Be Attended](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/)


        Given an array of events where events[i] = [startDayi, endDayi].
        Every event i starts at startDayi and ends at endDayi.

        You can attend an event i at any day d where startTimei <= d <= endTimei.
        Notice that you can only attend one event at any time d.

        Return the maximum number of events you can attend.

        **Example 1:**
        ```
        Input: events = [[1,2],[2,3],[3,4]]
        Output: 3
        Explanation: You can attend all the three events.
        One way to attend them all is as shown.
        Attend the first event on day 1.
        Attend the second event on day 2.
        Attend the third event on day 3.
        ```

        **Example 2:**
        ```
        Input: events= [[1,2],[2,3],[3,4],[1,2]]
        Output: 4
        ```

        **Example 3:**
        ```
        Input: events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
        Output: 4
        ```

        **Example 4:**
        ```
        Input: events = [[1,100000]]
        Output: 1
        ```

        **Example 5:**
        ```
        Input: events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
        Output: 7
        ```

        **Constraints:**
        - 1 <= events.length <= 10^5
        - events[i].length == 2
        - 1 <= events[i][0] <= events[i][1] <= 10^5

                Parameters
        ----------
        left: int
        right: int
        threshold: int

        Returns
        -------
        int

        Examples
        --------
        >>> sol = Solution()
        >>> sol.maxEvents([[1, 2], [2, 3], [3, 4]])
        3
        >>> sol.maxEvents([[1, 2], [2, 3], [3, 4], [1, 2]])
        4
        >>> sol.maxEvents([[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]])
        7

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/discuss/510263/JavaC%2B%2BPython-Priority-Queue

        """
        from heapq import heappush, heappop
        events.sort(reverse=True)
        h = []
        res, day = 0, 0
        while events or h:
            if not h:
                day = events[-1][0]
            while events and events[-1][0] <= day:
                heappush(h, events.pop()[1])
            heappop(h)
            res += 1
            day += 1
            while h and h[0] < day:
                heappop(h)
        return res

