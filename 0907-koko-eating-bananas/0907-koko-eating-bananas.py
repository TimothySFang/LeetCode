class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        
        def can_finish(k):
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k
                if hours > h:
                    return False
            return hours <= h
        
        while low < high:
            mid = (low + high) // 2
            if can_finish(mid):
                high = mid
            else:
                low = mid + 1
        return low