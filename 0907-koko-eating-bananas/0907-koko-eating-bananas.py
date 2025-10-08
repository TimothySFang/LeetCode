class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canFinish(hours):
            running_total = 0
            for p in piles:
                running_total += (p + hours - 1) // hours
            
            if running_total > h:
                return False
            else:
                return True
        
        small, large = 1, max(piles)
        result = 0
        while small <= large:
            mid = (small + large) // 2
            
            if canFinish(mid):
                # search for smaller / go left
                large = mid - 1
                result = mid
            else:
                small = mid + 1
        return result