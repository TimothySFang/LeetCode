class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0 :
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) <= 3:
            return max(nums)

        dp_oneInclusive = [0] * (len(nums) - 1)
        dp_twoInclusive = [0] * (len(nums) - 1)

        dp_oneInclusive[0] = nums[0]
        dp_oneInclusive[1] = max(nums[0], nums[1])
        dp_twoInclusive[0] = nums[1]
        dp_twoInclusive[1] = max(nums[1], nums[2])

        for i in range(2, len(nums) - 1):
            dp_oneInclusive[i] = max(dp_oneInclusive[i - 1], (dp_oneInclusive[i - 2] + nums[i]))
            dp_twoInclusive[i] = max(dp_twoInclusive[i - 1], (dp_twoInclusive[i - 2] + nums[i + 1]))

        print(dp_twoInclusive)
        return max(dp_twoInclusive[-1], dp_oneInclusive[-1]) 
        

