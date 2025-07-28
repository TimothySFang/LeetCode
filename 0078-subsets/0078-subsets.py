class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        soln = []
        def backtrackSubsets(start, path):
            soln.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrackSubsets(i + 1, path)
                path.pop()
        backtrackSubsets(0, [])
            
        return soln