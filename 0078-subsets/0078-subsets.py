class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        soln = [[]]
        def backtrackSubsets(nums):
            nonlocal soln
            if len(nums) == 0:
                # basecase (end state)
                return soln
            
            curr = nums.pop()
            soln_copy = [s[:] for s in soln]
            for n in range(len(soln_copy)):
                soln_copy[n].append(curr)
            soln = soln + soln_copy
            # ^ added all possible permutes for curr
            return backtrackSubsets(nums)

        return backtrackSubsets(nums)


            
