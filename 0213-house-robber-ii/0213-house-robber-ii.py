class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo_array_1 = {}
        memo_array_2 = {}

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        for i in range(1, len(nums)):
            if i == 1:
                memo_array_1[i] = nums[i]
            elif i == 2:
                memo_array_1[i] = max(memo_array_1[i - 1], nums[i])
            else:
                memo_array_1[i] = max(memo_array_1[i - 2] + nums[i], memo_array_1[i - 1])
        
        for i in range(0, len(nums) - 1):
            if i == 0:
                    memo_array_2[i] = nums[i]
            elif i == 1:
                memo_array_2[i] = max(memo_array_2[i - 1], nums[i])
            else:
                memo_array_2[i] = max(memo_array_2[i - 2] + nums[i], memo_array_2[i - 1])

        return max(memo_array_1[len(nums) - 1], memo_array_2[len(nums) - 2])