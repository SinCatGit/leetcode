from typing import List


class TwoSum:
    """
    https://leetcode.com/problems/two-sum-iii-data-structure-design/

    Design and implement a TwoSum class. It should support the following operations:add and find.

    add - Add the number to an internal data structure.
    find - Find if there exists any pair of numbers which sum is equal to the value.

    For example,
    add(1); add(3); add(5);
    find(4) -> true
    find(7) -> false

    References
    ---------
    .. [1] https://www.cnblogs.com/grandyang/p/5184143.html
    .. [2] https://leetcode.com/problems/two-sum-iii-data-structure-design/discuss/52034/Fast-and-simple-AC-Python
    .. [3] https://leetcode.com/problems/two-sum-iii-data-structure-design/discuss/52005/Trade-off-in-this-problem-should-be-considered

    """
    def __init__(self):
        from collections import defaultdict

        def zero():
            return 0

        self.ctr = defaultdict(zero)

    def add(self, num):
        self.ctr[num] += 1

    def find(self, target):
        ctr = self.ctr
        return any(target-num in ctr and (target-num != num or ctr[num] > 1) for num in ctr)
















