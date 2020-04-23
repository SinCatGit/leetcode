

class Solution:
    def countAndSay(self, n: int) -> str:
        """
        #### [38. Count and Say](https://leetcode.com/problems/count-and-say/)

        The count-and-say sequence is the sequence of integers with the first five terms as following:

        ```
        1.     1
        2.     11
        3.     21
        4.     1211
        5.     111221
        ```

        `1` is read off as `"one 1"` or `11`.
         `11` is read off as `"two 1s"` or `21`.
         `21` is read off as `"one 2`, then `one 1"` or `1211`.

        Given an integer *n* where 1 ≤ *n* ≤ 30, generate the *n*th term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

        Note: Each term of the sequence of integers will be represented as a string.



        **Example 1:**

        ```
        Input: 1
        Output: "1"
        Explanation: This is the base case.
        ```

        **Example 2:**

        ```
        Input: 4
        Output: "1211"
        Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1", "2" can be read as "12" which means frequency = 1 and value = 2, the same way "1" is read as "11", so the answer is the concatenation of "12" and "11" which is "1211".
        ```

        Parameters
        ----------
        n: int

        Returns
        -------
        str

        Examples
        --------

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/count-and-say/discuss/16044/Simple-Python-Solution
        .. [2] https://leetcode.com/problems/count-and-say/discuss/15999/4-5-lines-Python-solutions

        """
        from itertools import groupby
        s = '1'
        for _ in range(n-1):
            s = ''.join([str(len(list(g))) + k for k, g in groupby(s)])
        return s

    def countAndSayV01(self, n: int) -> str:
        s = '1'
        for _ in range(n-1):
            temp, count = [], 1
            for index in range(1, len(s)):
                if s[index] == s[index-1]:
                    count += 1
                else:
                    temp.append(str(count)+s[index-1])
                    count = 1
            temp.append(str(count)+s[-1])
            s = ''.join(temp)
        return s

