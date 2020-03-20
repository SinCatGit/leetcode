from typing import List


class Solution:
    def alienOrder(self, words: List[str]):
        """
        [269. Alien Dictionary](https://leetcode.com/problems/alien-dictionary)

        There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

        Example 1:

        ```
        Input:
        [
          "wrt",
          "wrf",
          "er",
          "ett",
          "rftt"
        ]

        Output: "wertf"
        ```

        Example 2:

        ```
        Input:
        [
          "z",
          "x"
        ]

        Output: "zx"
        ```

        Example 3:

        ```
        Input:
        [
          "z",
          "x",
          "z"
        ]

        Output: ""

        Explanation: The order is invalid, so return "".
        ```

        Note:

        1. You may assume all letters are in lowercase.
        2. You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
        3. If the order is invalid, return an empty string.
        4. There may be multiple valid order of letters, return any one of them is fine.
        """
        less = []
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    less += a + b,
                    break
        chars = set(''.join(words))
        pending = chars - set(''.join(less))
        chars -= pending
        order = []
        while less:
            free = chars - set(list(zip(*less))[1])
            if not free:
                return ''
            order += free
            less = list(filter(free.isdisjoint, less))
            chars -= free
        order += list(chars)
        for c in pending:
            i = 0
            while i < len(order):
                if order[i] > c:
                    order.insert(i, c)
                    break
                i += 1
            if i == len(order):
                order.append(c)
        return ''.join(order)