class Solution(object):
    from collections import defaultdict

    def countStairsMemo(self, n, memo):
        if memo[n] > 0 :
            return memo[n]

        memo[n] = self.countStairsMemo(n - 1, memo) + self.countStairsMemo(n - 2, memo)
        return memo[n]

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        memo = defaultdict(lambda: -1)
        memo[1] = 1
        memo[2] = 2
        memo[3] = 3
        return self.countStairsMemo(n, memo)

