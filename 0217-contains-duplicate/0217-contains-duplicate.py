class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        visited = {}
        for n in nums:
            if n in visited:
                return True
            else: visited[n] = 1
        return False