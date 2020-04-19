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
        from collections import defaultdict, deque
        edges = defaultdict(set)
        degrees = {c: 0 for c in set(''.join(words))}

        for word1, word2 in zip(words, words[1:]):
            found = False
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    found = True
                    if c2 not in edges[c1]:
                        degrees[c2] += 1
                    edges[c1].add(c2)
                    break

            if not found and len(word1) > len(word2):
                return ''

        queue = deque([c for c, val in degrees.items() if val == 0])
        result = []
        while queue:
            c = queue.popleft()
            result.append(c)
            for e in edges[c]:
                degrees[e] -= 1
                if not degrees[e]:
                    queue.append(e)

        return ''.join(result) if len(result) == len(degrees) else ''


    def alienOrderV01(self, words: List[str]):
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
