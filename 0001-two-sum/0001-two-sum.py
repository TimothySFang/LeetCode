class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for index, n in enumerate(nums):
            compliment = target - n
            if compliment in visited:
                return [index, visited[compliment]]
            else:
                visited[n] = index