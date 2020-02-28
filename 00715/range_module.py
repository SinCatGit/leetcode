from typing import List


class RangeModule:
    """
    [715. Range Module](https://leetcode.com/problems/range-module/)

    A Range Module is a module that tracks ranges of numbers. Your task is
    to design and implement the following interfaces in an efficient manner.

    - addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.
    - queryRange(int left, int right) Returns true if and only if every real number in the interval [left, right) is currently being tracked.
    - removeRange(int left, int right) Stops tracking every real number currently being tracked in the interval [left, right).

    **Example 1:**

    ```
    addRange(10, 20): null
    removeRange(14, 16): null
    queryRange(10, 14): true (Every number in [10, 14) is being tracked)
    queryRange(13, 15): false (Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
    queryRange(16, 17): true (The number 16 in [16, 17) is still being tracked, despite the remove operation)
    ```

    **Note:**

    - A half open interval [left, right) denotes all real numbers left <= x < right.
    - 0 < left < right < 10^9 in all calls to addRange, queryRange, removeRange.
    - The total number of calls to addRange in a single test case is at most 1000.
    - The total number of calls to queryRange in a single test case is at most 5000.
    - The total number of calls to removeRange in a single test case is at most 1000.

    References
    ----------
    .. [1] https://www.youtube.com/watch?v=pcpB9ux3RrQ
    .. [2] https://leetcode.com/problems/range-module/discuss/169353/Ultra-concise-Python-(only-6-lines-of-actual-code)-(also-236ms-beats-100)

    """

    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        res = []
        is_inserted = False
        for item in self.ranges:
            if item[1] < left:
                res += item,
            elif item[0] > right:
                if not is_inserted:
                    res += (left, right),
                    is_inserted = True
                res += item,
            else:
                left = min(left, item[0])
                right = max(right, item[1])
        if not is_inserted:
            res += (left, right),

        self.ranges = res

    def queryRange(self, left: int, right: int) -> bool:
        l, r = 0, len(self.ranges)-1
        while l <= r:
            mid = l + (r-l)//2
            if self.ranges[mid][0] > right:
                r = mid - 1
            elif self.ranges[mid][1] < left:
                l = mid + 1
            else:
                return self.ranges[mid][0] <= left and self.ranges[mid][1] >= right
        return False

    def removeRange(self, left: int, right: int) -> None:
        res = []
        for item in self.ranges:
            if item[1] < left:
                res += item,
            elif item[0] > right:
                res += item,
            else:
                if left > item[0]:
                    res += (item[0], left),
                if right < item[1]:
                    res += (right, item[1]),
        self.ranges = res


from bisect import bisect_left as bl, bisect_right as br


class RangeModuleV01:

    def __init__(self):
        self._X = []

    def addRange(self, left, right):
        i, j = bl(self._X, left), br(self._X, right)
        self._X[i:j] = [left]*(i%2 == 0) + [right]*(j%2 == 0)

    def queryRange(self, left, right):
        i, j = br(self._X, left), bl(self._X, right)
        return i == j and i%2 == 1

    def removeRange(self, left, right):
        i, j = bl(self._X, left), br(self._X, right)
        self._X[i:j] = [left]*(i%2 == 1) + [right]*(j%2 == 1)


if __name__ == '__main__':
    # r = RangeModule()
    # r.addRange(10, 20)
    # print(r.ranges)
    # r.removeRange(14, 16)
    # print(r.ranges)
    # print(r.queryRange(10, 14))
    # print(r.queryRange(13, 15))
    # print(r.queryRange(16, 17))

    # ["RangeModule", "addRange", "addRange", "addRange", "queryRange", "queryRange", "queryRange", "removeRange",
    #  "queryRange"]
    # [[], [10, 180], [150, 200], [250, 500], [50, 100], [180, 300], [600, 1000], [50, 150], [50, 100]]

    r = RangeModule()
    r.addRange(10, 180)
    print(r.ranges)
    r.addRange(150, 200)
    print(r.ranges)
    r.addRange(250, 500)
    print(r.ranges)
    print(r.queryRange(50, 100))
    print(r.queryRange(180, 300))
    print(r.queryRange(600, 1000))
    r.removeRange(50, 150)
    print(r.ranges)
    print(r.queryRange(50, 100))






