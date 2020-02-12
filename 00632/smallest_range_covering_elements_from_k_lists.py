import heapq

from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        """
        https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

        You have k lists of sorted integers in ascending order. Find the smallest range that
        includes at least one number from each of the k lists.

        We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

        Parameters
        ----------
        nums: List[List[int]]

        Returns
        -------
        List[int]

        Examples
        --------
        >>> sol = Solution()
        >>> sol.smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]])
        [20, 24]

        Notes
        -----

        References
        ---------
        .. [1] https://www.youtube.com/watch?v=Fqal25ZgEDo
        .. [2] https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/discuss/104904/Python-Heap-based-solution
        .. [3] https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/discuss/258013/Python-Sliding-Window-easy-to-understand

        """
        res = [float('-inf'), float('inf')]
        merge_nums = list()
        k = len(nums)
        for i, l in enumerate(nums):
            for n in l:
                merge_nums.append((n, i))
        merge_nums.sort()
        d = {}
        left, count = 0, 0
        for right, item in enumerate(merge_nums):
            rv, ri = item
            d[ri] = d.get(ri, 0) + 1
            if d[ri] == 1:
                count += 1
            while count == k:
                lv, li = merge_nums[left]
                if rv - lv < res[1] - res[0]:
                    res = [lv, rv]
                d[li] -= 1
                left += 1
                if d[li] == 0:
                    count -= 1
        return res

    def smallestRangeV01(self, nums: List[List[int]]) -> List[int]:

        res = list()
        min_range = float('inf')
        min_heap = [(l[0], 0, i) for i, l in enumerate(nums)]
        heapq.heapify(min_heap)
        max_val, _, _ = heapq.nlargest(1, min_heap)[0]
        while len(min_heap) == len(nums):
            min_val, j, i = min_heap[0]

            if max_val - min_val < min_range:
                res = [min_val, max_val]
                min_range = max_val - min_val
            heapq.heappop(min_heap)
            if j + 1 < len(nums[i]):
                max_val = max(max_val, nums[i][j+1])
                heapq.heappush(min_heap, (nums[i][j+1], j+1, i))

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
    print(sol.smallestRange([[1, 2, 3], [1, 2, 3]]))
    print(sol.smallestRange([[1],[2],[3],[4],[5],[6],[7]]))
    print(sol.smallestRange([[1],[2], [3], [5], [4], [6], [7]]))
    print(sol.smallestRange([[1],[2], [3], [5], [4], [6], [7], [8]]))
    print(sol.smallestRange([[1],[2], [3], [5], [4], [6], [7], [8], [9]]))

