from typing import List


class NumArray:
    """
    [307. Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/)


    Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

    The update(i, val) function modifies nums by updating the element at index i to val.

    **Example:**

    ```
    Given nums = [1, 3, 5]

    sumRange(0, 2) -> 9
    update(1, 2)
    sumRange(0, 2) -> 8
    ```

    **Note:**

    1. The array is only modifiable by the update function.
    2. You may assume the number of calls to update and sumRange function is distributed evenly.

    """

    def __init__(self, nums: List[int]):
        self.nums_len = len(nums) + 1
        self.nums = [0]*self.nums_len
        self.bit = [0]*self.nums_len
        list(map(self.update, range(self.nums_len-1), nums))

    def update(self, i: int, val: int) -> None:
        i += 1
        diff, self.nums[i] = val-self.nums[i], val
        while i < self.nums_len:
            self.bit[i] += diff
            i += i & -i

    def sumRange(self, i: int, j: int) -> int:
        return self._pre_sum(j) - self._pre_sum(i-1)

    def _pre_sum(self, i: int) -> int:
        i += 1
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res


if __name__ == '__main__':
    num_array = NumArray([1, 2, 3, 4, 5, 6, 7, 8, 9])

    for item in num_array.bit:
        print(item, end=' ')
    print()
    print(num_array.sumRange(1, 3))
    print(num_array.sumRange(6, 8))

