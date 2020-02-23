from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        https://leetcode.com/problems/letter-combinations-of-a-phone-number

        Given a string containing digits from 2-9 inclusive, return all possible letter
        combinations that the number could represent.

        A mapping of digit to letters (just like on the telephone buttons) is given below.
        Note that 1 does not map to any letters.


        Example:

        Input: "23"
        Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
        Note:

        Although the above answer is in lexicographical order, your answer could be in any order you want.


        Parameters
        ----------
        digits: str

        Returns
        -------
        List[str]

        Examples
        --------
        >>> sol = Solution()
        >>> sorted(sol.letterCombinations('23'))
        ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8070/One-line-python-solution

        """
        if not digits:
            return []
        kv = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        from functools import reduce

        return reduce(lambda acc, d: [x+y for y in kv[d] for x in acc], digits, [''])

    def letterCombinationsV01(self, digits: str) -> List[str]:
        if not digits:
            return []
        kv = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        from itertools import product

        return [''.join(r) for r in product(*(kv[d] for d in digits))]


