class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]

        for i in range(len(nums)):
            temp_ans = []
            for j in range(len(ans)):
                temp_ans.append(ans[j])
                temp_ans.append(ans[j] + [nums[i]])
            ans = temp_ans

        return ans