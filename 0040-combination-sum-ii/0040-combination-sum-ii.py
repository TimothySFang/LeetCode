class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()

        def backtrack(start, path, total):
            if total == target:
                result.append(path)
            
            if total > target:
                return
            
            prev = -1 
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue
                
                backtrack(i + 1, path + [candidates[i]], total + candidates[i])

                prev = candidates[i]

        backtrack(0, [], 0)
        return result
        
            