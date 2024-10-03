class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = {}

        max = 0
        ret_value = 0
        for n in nums:
            if n in visited:
                visited[n] += 1
            else:
                visited[n] = 1
        for value in visited:
            if visited[value] > max:
                max = visited[value]
                ret_value = value
        return ret_value