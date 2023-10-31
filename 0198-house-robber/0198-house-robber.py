class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo_array = {}

        for i in range(len(nums)):
            if i == 0:
                memo_array[0] = nums[i]
            elif i == 1:
                memo_array[1] = max(nums[i], memo_array[0])
            else:
                memo_array[i] = max(nums[i] + memo_array[i - 2], memo_array[i - 1])
        
        return memo_array[len(nums) - 1]