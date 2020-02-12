

class Solution:
    def reorganizeString(self, S: str) -> str:
        """
        https://leetcode.com/problems/reorganize-string/

        Given a string S, check if the letters can be rearranged so that two characters
        that are adjacent to each other are not the same.

        If possible, output any possible result.  If not possible, return the empty string.

        Parameters
        ----------
        S: str

        Returns
        -------
        str

        Examples
        --------
        >>> sol = Solution()
        >>> sol.reorganizeString('aab')
        'aba'

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode-cn.com/problems/reorganize-string/solution/zhong-gou-zi-fu-chuan-by-leetcode/

        """
        d = {}
        total = 0
        for ch in S:
            d[ch] = d.get(ch, 0) + 1
            total += 1

        pairs = [(v, k) for k, v in d.items()]
        pairs.sort()
        max_v, max_ch = pairs[-1]
        if max_v - 1 > total - max_v:
            return ''
        A = list()
        for v, k in pairs:
            A.extend(v*k)
        ans = ['']*total
        ans[::2], ans[1::2] = A[total//2:], A[:total//2]

        return ''.join(ans)

    def reorganizeStringV01(self, S: str) -> str:
        import heapq
        pq = [(-S.count(c), c) for c in set(S)]
        heapq.heapify(pq)
        total = sum([-1*cnt for cnt, _ in pq])
        if total + pq[0][0] < -pq[0][0]-1:
            return ''
        ans = list()
        while len(pq) >= 2:
            cnt1, ch1 = heapq.heappop(pq)
            cnt2, ch2 = heapq.heappop(pq)
            ans.extend([ch1, ch2])
            if cnt1 + 1:
                heapq.heappush(pq, (cnt1+1, ch1))
            if cnt2 + 1:
                heapq.heappush(pq, (cnt2+1, ch2))
        return ''.join(ans) + (pq[0][1] if pq else '')


if __name__ == '__main__':
    sol = Solution()
    print(sol.reorganizeString('aab'))

