class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lower, upper = float('inf'), 0
        max_prof = 0

        for p in prices:
            if p < lower:
                lower = p
                upper = 0
            if p > upper:
                upper = p
                if upper - lower > max_prof:
                    max_prof = upper - lower
        return max_prof

            