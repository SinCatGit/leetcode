from typing import List
from collections import defaultdict


class Solution:
    def replaceWords(self, d: List[str], sentence: str) -> str:
        """
        https://leetcode.com/problems/replace-words/

        In English, we have a concept called root, which can be followed by some other words to
        form another longer word - let's call this word successor. For example, the root an,
        followed by other, which can form another word another.

        Now, given a dictionary consisting of many roots and a sentence. You need to replace
        all the successor in the sentence with the root forming it. If a successor has many roots can form it,
        replace it with the root with the shortest length.

        You need to output the sentence after the replacement.

        Parameters
        ----------
        d: List[str]
        sentence: str

        Returns
        -------
        str

        Examples
        --------
        >>> sol = Solution()
        >>> sol.replaceWords(['cat', 'bat', 'rat'], 'the cattle was rattled by the battery')
        'aba'

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode-cn.com/problems/reorganize-string/solution/zhong-gou-zi-fu-chuan-by-leetcode/

        """
        trie = Trie()
        for w in d:
            trie.add_prefix(w)
        res = []
        for w in sentence.split(' '):
            prefix = trie.search(w)
            if prefix:
                res.append(prefix)
            else:
                res.append(w)

        return ' '.join(res)


class Trie:
    def __init__(self):
        self.root = defaultdict()
        self.END_CHAR = '#'

    def add_prefix(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, defaultdict())
        node[self.END_CHAR] = self.END_CHAR

    def search(self, word: str) -> str:
        node = self.root
        res = ''
        for ch in word:
            if self.END_CHAR in node:
                return res
            if ch not in node:
                break
            node = node[ch]
            res += ch
        return ''


if __name__ == '__main__':
    sol = Solution()
    print(sol.replaceWords(['cat', 'bat', 'rat'], 'the cattle was rattled by the battery'))

