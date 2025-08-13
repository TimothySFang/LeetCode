class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)

        def can_finish(k: int) -> bool:
            # hours needed at speed k
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k  # ceil(p / k) without floats
                if hours > h:              # early break if already too many hours
                    return False
            return hours <= h

        while lo < hi:
            mid = (lo + hi) // 2
            if can_finish(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo