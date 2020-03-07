class Solution:
    def countPrimes(self, n: int) -> int:
        """
        [204. Count Primes](https://leetcode.com/problems/count-primes/)

        Count the number of prime numbers less than a non-negative number, *n*.

        **Example:**

        ```
        Input: 10
        Output: 4
        Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
        ```

        """
        if n <= 2:
            return 0
        res = [1]*n
        res[0], res[1] = 0, 0
        for i in range(2, int(n**0.5)+1):
            if res[i] == 1:
                res[i*i:n:i] = [0]*(len(res[i*i:n:i]))

        return sum(res)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countPrimes(499979))
