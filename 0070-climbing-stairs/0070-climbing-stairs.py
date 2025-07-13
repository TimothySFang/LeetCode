class Solution:
    def climbStairs(self, n: int) -> int:
        def memoizeStairs(memo, n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = memoizeStairs(memo, n - 1) + memoizeStairs(memo, n - 2)
                return memo[n]
        memo = {}
        memo[1] = 1
        memo[2] = 2
        return memoizeStairs(memo, n)