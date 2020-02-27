from typing import List


class BITree:
    def __init__(self, n):
        self.n = n + 1
        self.bit = [0]*self.n

    def update(self, i: int) -> None:
        i += 1
        while i < self.n:
            self.bit[i] += 1
            i += i & -i

    def pre_sum(self, i: int) -> int:
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """
        [493. Reverse Pairs](https://leetcode.com/problems/reverse-pairs/)


        Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

        You need to return the number of important reverse pairs in the given array.

        **Example1:**

        ```
        Input: [1,3,2,3,1]
        Output: 2
        ```

        **Example2:**


        ```
        Input: [2,4,3,5,1]
        Output: 3
        ```

        **Note:**

        The length of the given array will not exceed 50,000.
        All the numbers in the input array are in the range of 32-bit integer.

        Parameters
        ----------
        nums: List[int]

        Returns
        -------
        int

        Examples
        --------

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/reverse-pairs/discuss/162757/Python-BIT-using-ranks-Clear-O(nlog(n))


        """
        d = {v: i for i, v in enumerate(sorted(set(nums+[2*v for v in nums])))}
        cnt = 0
        btree = BITree(len(d))
        for n in nums[::-1]:
            rank = d[2*n]
            cnt += btree.pre_sum(d[n])
            btree.update(rank)
        return cnt


if __name__ == '__main__':
    sol = Solution()
    print(sol.reversePairs([5, 2, 6, 1]))
