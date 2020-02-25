from typing import List


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        """
        https://leetcode.com/problems/palindrome-permutation_ii

        Given a string s, return all the palindromic permutations (without duplicates) of it.
        Return an empty list if no palindromic permutation could be form.

        Example 1:

        Input: "aabb"
        Output: ["abba", "baab"]
        Example 2:

        Input: "abc"
        Output: []

        Parameters
        ----------
        s: str

        Returns
        -------
        bool

        Examples
        --------
        >>> sol = Solution()
        >>> sol.generatePalindromes('aabb')
        ['abba', 'baab']
        >>> sol.generatePalindromes('abc')
        []

        Notes
        -----

        References
        ---------
        .. [1] https://www.cnblogs.com/grandyang/p/5315227.html
        .. [2]

        """
        from collections import Counter
        self.count = Counter(s)
        self.odd_char = ''
        self.ans = []
        for k, v in self.count.items():
            if v % 2 == 1 and self.odd_char != '':
                return []

            if v % 2 == 1 and self.odd_char == '':
                self.odd_char = k

            self.count[k] = v // 2

        def dfs(path, left=len(s)//2):
            if left == 0:
                self.ans.append(path+self.odd_char+path[::-1])
            for k in self.count:
                if self.count[k]:
                    self.count[k] -= 1
                    dfs(path+k, left-1)
                    self.count[k] += 1

        dfs('')
        return self.ans






