from typing import List


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/rectangle-area-ii/

        [850. Rectangle Area II](https://leetcode.com/problems/rectangle-area-ii/)

        We are given a list of (axis-aligned) rectangles.  Each rectangle[i] = [x1, y1, x2, y2] ,
        where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates
        of the top-right corner of the ith rectangle.

        Find the total area covered by all rectangles in the plane.  Since the answer may be too large,
        return it modulo 10^9 + 7.


        **Example 1:**
        ```
        Input: [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
        Output: 6
        Explanation: As illustrated in the picture.
        ```
        **Example 2:**
        ```
        Input: [[0,0,1000000000,1000000000]]
        Output: 49
        Explanation: The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 = (-7)^2 = 49.
        ```

        **Note:**

        - 1 <= rectangles.length <= 200
        - rectanges[i].length = 4
        - 0 <= rectangles[i][j] <= 10^9
        - The total area covered by all rectangles will never exceed 2^63 - 1 and thus will fit in a 64-bit signed integer.


        Parameters
        ----------
        rectangles: List[List[int]]

        Returns
        -------
        int

        Examples
        --------
        >>> sol = Solution()
        >>> sol.rectangleArea([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]])
        6
        >>> sol.rectangleArea([[0,0,1000000000,1000000000]])
        49

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/rectangle-area-ii/discuss/137914/C%2B%2BPython-Discretization-and-O(NlogN)
        .. [2] https://leetcode.com/problems/rectangle-area-ii/discuss/226266/concise-python-40ms-beats-100

        """
        area = 0
        rects = [item for x1, y1, x2, y2 in rectangles for item in [[x1, y1, y2, 0], [x2, y1, y2, 1]]]
        last = rects[0][0]
        heap = [(float('inf'), float('inf'))]
        for x, y1, y2, k in sorted(rects):
            h = start = end = 0
            for m, n in heap:
                if m > end:
                    h += end - start
                    start, end = m, n
                else:
                    end = max(end, n)
            area += (x-last)*h
            import bisect
            heap.remove((y1, y2)) if k else bisect.insort(heap, (y1, y2))
            last = x

        return area % (10**9 + 7)

    def rectangleAreaV01(self, rectangles: List[List[int]]) -> int:

        xs = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]]))
        count = [0]*len(xs)
        xi = {v: i for i, v in enumerate(xs)}
        L = []
        for x1, y1, x2, y2 in rectangles:
            L.append((y1, x1, x2, 1))
            L.append((y2, x1, x2, -1))
        L.sort()

        cur_sum = 0
        area = 0
        cur_y = 0

        for y, x1, x2, sig in L:
            area += (y-cur_y)*cur_sum
            cur_y = y
            for i in range(xi[x1], xi[x2]):
                count[i] += sig
            cur_sum = sum(x2-x1 if c else 0 for x1, x2, c in zip(xs, xs[1:], count))
        return area % (10 ** 9 + 7)




