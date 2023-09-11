class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        for i in range(len(nums)):
            target = -1 * nums[i]
            target_index = i
            visited = {}
            for j in range(i, len(nums)):
                if (j != target_index):
                    if (target - nums[j]) in visited:
                        potAns = [-1 * target, nums[j], (target - nums[j])]
                        potAns.sort()
                        if potAns not in result: 
                            result.append(potAns)
                    else: visited[nums[j]] = nums[j]
        return result