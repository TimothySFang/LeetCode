class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if lower than left index, left = index. 

        left = 0
        right = 0
        max_prof = 0
        while right < len(prices):
            value = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_prof = max(value, max_prof)
            else :
                left = right
            right += 1
        return max_prof