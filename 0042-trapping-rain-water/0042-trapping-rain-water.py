class Solution:
    def trap(self, height: List[int]) -> int:
        l, water = 0, 0
        r = len(height) - 1
        lm, rm = height[l], height[r]

        while l < r:
            if lm <= rm:
                l += 1                              # move first
                lm = max(lm, height[l])       # update cap
                water += lm - height[l]          # add water at new l
            else:
                r -= 1
                rm = max(rm, height[r])
                water += rm - height[r]
        return water