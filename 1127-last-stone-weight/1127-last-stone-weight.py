class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg = [-x for x in stones]
        heapq.heapify(neg)
        while len(neg) > 1:
            s1 = heapq.heappop(neg)
            s2 = heapq.heappop(neg)
            s1 = s1 - s2
            print(s1)
            if s1 < 0:
                heapq.heappush(neg, s1)
                
        if len(neg) == 1:
            return -neg[0]
        else:
            return 0