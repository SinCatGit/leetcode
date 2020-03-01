from typing import List
from collections import defaultdict
from bisect import bisect_left as bl
from bisect import bisect_right as br
from random import randint


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        a2i = defaultdict(list)
        for i, a in enumerate(arr):
            a2i[a] += i,
        self.a2i = a2i

    def query(self, left: int, right: int, threshold: int) -> int:
        """
        [1157. Online Majority Element In Subarray](https://leetcode.com/problems/online-majority-element-in-subarray/)

        Implementing the class MajorityChecker, which has the following API:

        - MajorityChecker(int[] arr) constructs an instance of MajorityChecker with the given array arr;
        - int query(int left, int right, int threshold) has arguments such that:
            - 0 <= left <= right < arr.length representing a subarray of arr;
            - 2 * threshold > right - left + 1, ie. the threshold is always a strict majority of the length of the subarray

        Each query(...) returns the element in arr[left], arr[left+1], ..., arr[right] that occurs at least threshold times, or -1 if no such element exists.

        **Example:**
        ```
        MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
        majorityChecker.query(0,5,4); // returns 1
        majorityChecker.query(0,3,3); // returns -1
        majorityChecker.query(2,3,2); // returns 2
        ```

        **Constraints:**

        - 1 <= arr.length <= 20000
        - 1 <= arr[i] <= 20000
        - For each query, 0 <= left <= right < len(arr)
        - For each query, 2 * threshold > right - left + 1
        - The number of queries is at most 10000

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
        >>> sol = MajorityChecker([1, 1, 2, 2, 1, 1])
        >>> sol.query(0, 5, 4)
        1
        >>> sol.query(0, 3, 3)
        -1
        >>> sol.query(2, 3, 2)
        2

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/online-majority-element-in-subarray/discuss/356115/Theory-O(n-log-n-log*-n%2B-m-log-n)-time-algorithm-n-is-the-array-size-m-is-the-number-of-queries
        .. [2] https://leetcode.com/problems/online-majority-element-in-subarray/discuss/355848/Python-Binary-Search-%2B-Find-the-Majority-Element
        .. [3] https://leetcode.com/problems/online-majority-element-in-subarray/discuss/360493/Python-Segment-tree-(merge-in-O(1)-query-O(log-n))

        """
        for _ in range(10):
            a = self.arr[randint(left, right)]
            l = bl(self.a2i[a], left)
            r = br(self.a2i[a], right)
            if r - l >= threshold:
                return a
        return -1

    def queryV01(self, left: int, right: int, threshold: int) -> int:
        cnt = 0
        candidate = self.arr[left]
        for i in range(left, right+1):
            if cnt == 0:
                candidate = self.arr[i]
                cnt += 1
            elif self.arr[i] == candidate:
                cnt += 1
            else:
                cnt -= 1

        return candidate if cnt > 0 else -1



