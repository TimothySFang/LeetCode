class Solution(object):
    def minCostClimb(self, cost, memo, index, accumulator_cost):

        # base case
        if (index == 0 or index == 1):
            return accumulator_cost + cost[index]
        
        # iterative section to find value of prev two index costs
        path_one = memo[index - 1] if memo[index - 1] != None else self.minCostClimb(cost, memo, index - 1, accumulator_cost)
        path_two = memo[index - 2] if memo[index - 2] != None else self.minCostClimb(cost, memo, index - 2, accumulator_cost)
        
        # adding to accumulated cost
        accumulator_cost += (min(path_one, path_two) + cost[index])
        memo[index] = accumulator_cost

        return memo[index]


    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        from collections import defaultdict

        visitedCostPaths = defaultdict(lambda: None)
        
        return min(self.minCostClimb(cost, visitedCostPaths, len(cost) - 1, 0), self.minCostClimb(cost, visitedCostPaths, len(cost) - 2, 0))
    