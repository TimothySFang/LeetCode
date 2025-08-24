class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        lm, rm = 0, 0
        water = 0
        while left < right:
            if (height[left] <= height[right]):
                lm = max(height[left], lm)
                if lm > height[left]:
                    water += lm - height[left]
                left += 1
            else:
                rm = max(height[right], rm)
                if rm > height[right]:
                    water += rm - height[right]
                right -= 1
        return water