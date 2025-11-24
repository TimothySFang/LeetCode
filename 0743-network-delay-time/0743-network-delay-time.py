class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))
        dist = [inf] * (n + 1)
        dist[k] = 0

        heap = [(0, k)]

        while heap:
            curr_time, u = heapq.heappop(heap)

            if curr_time > dist[u]:
                continue

            if curr_time > dist[u]:
                continue

            for v, w in graph[u]:
                new_time = curr_time + w
                if new_time < dist[v]:
                    dist[v] = new_time
                    heapq.heappush(heap, (new_time, v))
                
        max_dist = max(dist[1:])  # ignore index 0
        
        return -1 if max_dist == inf else max_dist