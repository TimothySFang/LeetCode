class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = {}
        for n in nums:
            if n in visited:
                return True
            else:
                visited[n] = 1
        return False