from typing import List

from bisect import bisect_right as br
from bisect import bisect_left as bl


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        height = [0]
        pos = [0]
        res = []
        max_h = 0
        for left, side in positions:
            i = br(pos, left)
            j = bl(pos, left + side)
            # print(f'i:{i}, j:{j}')
            high = max(height[i - 1:j] or [0]) + side
            # print(height, pos)
            pos[i:j] = [left, left + side]
            # print(f'high:{high}, height[j-1]:{height[j-1]}')
            height[i:j] = [high, height[j - 1]]
            # print(height, pos)
            max_h = max(max_h, high)
            res.append(max_h)
        return res


if __name__ == '__main__':
    sol = Solution()
    sol.fallingSquares([[1, 2], [2, 3], [6, 1], [5, 2]])
