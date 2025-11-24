class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        cost = [float('inf')] * (n + 1)
        cost[k] = 0
        graph = defaultdict(list)

        for t in times:
            graph[t[0]].append((t[1], t[2])) #source node = (target node, weight)

        heap = [(0, k)]

        while heap:
            curr_time, node = heapq.heappop(heap)

            if curr_time > cost[node]:
                continue
    
            for u, w in graph[node]:
                # u = node, w = weight
                if curr_time + w < cost[u]:
                    cost[u] = curr_time + w
                    heapq.heappush(heap, (curr_time + w, u))
        

        return -1 if max(cost[1:]) == float('inf') else max(cost[1:])
