class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        max_value = 0
        for n in numSet:
            if (n - 1) in numSet:
                continue
            else:
                counter = 1
                curr_longest = 1
                while (n + counter) in numSet:
                    curr_longest += 1
                    counter += 1
                max_value = max(curr_longest, max_value)
        return max_value