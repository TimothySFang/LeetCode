class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:    
        if len(cost) <= 2:
            return min(cost[0], cost[1])
        
        first, second = cost[0], cost[1]

        for i in range(2, len(cost)):
            second, first = min(first, second) + cost[i], second
        
        return min(second, first)