from typing import List
from heapq import heappush, heapreplace


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii)

        Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...]`
        (si < ei), find the minimum number of conference rooms required.

        Example 1:

        ```
        Input: [[0, 30],[5, 10],[15, 20]]
        Output: 2
        ```

        Example 2:

        ```
        Input: [[7,10],[2,4]]
        Output: 1
        ```

        **NOTE:** input types have been changed on April 15, 2019. Please reset to default code definition to
        get new method signature.


        Parameters
        ----------
        intervals: List[List[int]]

        Returns
        -------
        int

        Examples
        --------

        Notes
        -----

        References
        ---------
        .. [1]

        """
        hp = []
        intervals = sorted(intervals, key=lambda i: i[0])
        for s, e in intervals:
            if hp and s >= hp[0]:
                heapreplace(hp, e)
            else:
                heappush(hp, e)
        return len(hp)

