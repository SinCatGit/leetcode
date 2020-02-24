from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        https://leetcode.com/problems/combination-sum-iv

        Given an integer array with all positive numbers and no duplicates, find the
        number of possible combinations that add up to a positive integer target.

        Example:

        nums = [1, 2, 3]
        target = 4

        The possible combination ways are:
        (1, 1, 1, 1)
        (1, 1, 2)
        (1, 2, 1)
        (1, 3)
        (2, 1, 1)
        (2, 2)
        (3, 1)

        Note that different sequences are counted as different combinations.

        Therefore the output is 7.


        Follow up:
        What if negative numbers are allowed in the given array?
        How does it change the problem?
        What limitation we need to add to the question to allow negative numbers?


        Parameters
        ----------
        nums: List[int]
        target: int

        Returns
        -------
        int

        Examples
        --------
        >>> sol = Solution()
        >>> sol.combinationSum4([1, 2, 3], 4)
        7

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/combination-sum-iv/discuss/85041/7-liner-in-Python-and-follow-up-question

        """
        nums, combs = sorted(nums), [1]+[0]*target
        for i in range(target+1):
            for num in nums:
                if num > i:
                    break
                combs[i] += combs[i-num]
        return combs[target]

    def combinationSum4V01(self, nums: List[int], target: int) -> int:

        self.ans = []
        nums = sorted(nums)

        def backtrack(remain, target, path):
            if target == 0:
                self.ans.append(path)

            if not remain or remain[0] > target:
                return

            backtrack(remain, target - remain[0], path + [remain[0]])
            backtrack(remain[1:], target, path)

        backtrack(nums, target, [])
        def factor(n):
            if n == 1:
                return 1
            return factor(n-1)*n
        total = 0
        from functools import reduce
        from collections import Counter
        for item in self.ans:
            t = factor(len(item))
            acc = [factor(cnt) for cnt in Counter(item).values() if cnt > 1]
            total += reduce(lambda x, y: x/y, acc, t)

        return total


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum4([3, 33, 333], 10000))
