from typing import List


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """
        #### [340. Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)

        Given a string, find the length of the longest substring T that contains at most *k* distinct characters.

        **Example 1:**

        ```
        Input: s = "eceba", k = 2
        Output: 3
        Explanation: T is "ece" which its length is 3.
        ```

        **Example 2:**

        ```
        Input: s = "aa", k = 1
        Output: 2
        Explanation: T is "aa" which its length is 2.
        ```

        Parameters
        ----------
        s: str
        k: int

        Returns
        -------
        int

        Examples
        --------

        References
        ---------

        """
        from collections import OrderedDict
        i, max_len, index_map = 0, 0, OrderedDict()
        for j, c in enumerate(s, 1):
            index_map[c] = j
            index_map.move_to_end(c)
            if len(index_map) > k:
                _, i = index_map.popitem(last=False)
            max_len = max(max_len, j-i)
        return max_len

    def lengthOfLongestSubstringKDistinctV01(self, s: str, k: int) -> int:
        left, max_len = 0, 0
        cnt = 0
        from collections import Counter
        counts = Counter()
        for right, c in enumerate(s):
            counts[c] += 1
            if counts[c] == 1:
                cnt += 1
            while cnt > k:
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    cnt -= 1
                left += 1
            max_len = max(max_len, right-left+1)
        return max_len



