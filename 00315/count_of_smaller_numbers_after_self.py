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
    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        [315. Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)


        You are given an integer array nums and you have to return a new counts array. The counts
        array has the property where counts[i] is the number of smaller elements to the right of nums[i].

        **Example:**

        ```
        Input: [5,2,6,1]
        Output: [2,1,1,0]
        Explanation:
        To the right of 5 there are 2 smaller elements (2 and 1).
        To the right of 2 there is only 1 smaller element (1).
        To the right of 6 there is 1 smaller element (1).
        To the right of 1 there is 0 smaller element.
        ```

        Parameters
        ----------
        nums: List[int]

        Returns
        -------
        List[int]

        Examples
        --------

        Notes
        -----

        References
        ---------
        .. [1] https://www.youtube.com/watch?v=2SVLYsq5W8M
        .. [2] https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76657/3-ways-(Segment-Tree-Binary-Indexed-Tree-Binary-Search-Tree)-clean-python-code
        .. [3] https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76580/9ms-short-Java-BST-solution-get-answer-when-building-BST


        """
        d = {v: i for i, v in enumerate(sorted(set(nums)))}
        res = []
        btree = BITree(len(d))
        for n in nums[::-1]:
            rank = d[n]
            res.append(btree.pre_sum(rank))
            btree.update(rank)
        return res[::-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.countSmaller([5, 2, 6, 1]))
