class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = {}
        for n in nums:
            if n in visited:
                visited[n] += 1
            else:
                visited[n] = 1
        for n in visited:
            if visited[n] != 1:
                return True
        return False