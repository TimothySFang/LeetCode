class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x, y in points:
            
            #calc euclidean distance
            euclid = math.sqrt((x * x) + (y * y))
            heapq.heappush(min_heap, (-euclid, x, y))

            if len(min_heap) > k:
                euc = heapq.heappop(min_heap)

        results = []
        for dist, x, y in min_heap:
            results.append((x, y))

        return results