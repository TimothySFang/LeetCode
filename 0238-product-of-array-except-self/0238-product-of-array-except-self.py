class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_right = [1] * len(nums)
        prev = 1
        for i in range(len(nums) - 1):
            prev *= nums[i]
            left_right[i + 1] = prev

        prev = 1
        for i in range(len(nums) - 1, 0, -1):
            prev *= nums[i]
            left_right[i - 1] *= prev
        return left_right 