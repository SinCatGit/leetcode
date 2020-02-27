from typing import List


class BITree:
    def __init__(self, n: int):
        self.n = n + 1
        self.bit = [0]*self.n

    def update(self, i: int) -> None:
        while i < self.n:
            self.bit[i] += 1
            i += (i & -i)

    def pre_sum(self, i: int) -> int:
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= (i & -i)
        return res


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        #  lower <= sum[j]-sum[i] <= upper
        #  sum[i] >= sum[j]-upper and sum[i] <= sum[j]-lower
        #
        nums_len = len(nums)
        num_acc = [0]*(nums_len+1)
        for i in range(nums_len):
            num_acc[i+1] = num_acc[i] + nums[i]

        sort_acc = sorted(num_acc)
        btree = BITree(nums_len+1)
        res = 0
        import bisect
        for a in num_acc:
            lo, hi = bisect.bisect_left(sort_acc, a-upper), bisect.bisect_right(sort_acc, a-lower)
            res += btree.pre_sum(hi) - btree.pre_sum(lo)
            btree.update(bisect.bisect_left(sort_acc, a)+1)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.countRangeSum([-2, 5, -1], -2, 2))


