from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

        Given n non-negative integers representing an elevation map where the width of each bar is 1,
        compute how much water it is able to trap after raining.

        The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
        6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

        **Example:**

        ```
        Input: [0,1,0,2,1,0,1,3,2,1,2,1]
        Output: 6
        ```

        """
        ans = 0
        l, r = 0, len(height)-1
        maxl, maxr = height[0], height[-1]
        while l < r:
            if maxl < maxr:
                ans += maxl-height[l]
                l += 1
                maxl = max(maxl, height[l])
            else:
                ans += maxr - height[r]
                r -= 1
                maxr = max(maxr, height[r])
        return ans

    def trapV02(self, height: List[int]) -> int:
        ans = 0
        for i, h in enumerate(height):
            hl = max(height[:i+1])
            hr = max(height[i:])
            ho = min(hl, hr)
            ans += ho - h
        return ans

    def trapV01(self, height: List[int]) -> int:
        if not height:
            return 0
        hlen = len(height)
        dpl, dpr = [0]*hlen, [0]*hlen
        dpl[0], dpr[-1] = height[0], height[-1]
        for i in range(1, hlen):
            dpl[i] = max(height[i], dpl[i-1])
            dpr[-i-1] = max(height[-i-1], dpr[-i])
        ans = 0
        for i, h in enumerate(height):
            ans += min(dpl[i], dpr[i]) - h
        return ans
