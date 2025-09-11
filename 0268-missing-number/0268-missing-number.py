class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        visited = {}

        for n in range(len(nums)):
            visited[nums[n]] = 1
        
        for i in range(len(visited) + 1):
            if i not in visited:
                return i
