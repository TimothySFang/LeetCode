class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        jumps = 0
        while i < len(nums) - 1:
            j = nums[i]
            jump_range = i + j

            if jump_range >= len(nums) - 1:
                return jumps + 1

            max_jump = 0
            max_index = i

            for x in range(i + 1, jump_range + 1):
                if (x + nums[x]) >= max_jump:
                    max_jump = x + nums[x]
                    max_index = x

            i = max_index
            jumps += 1
        return jumps