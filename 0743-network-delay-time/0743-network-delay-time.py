class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        cost = [float('inf')] * (n + 1)
        cost[k] = 0
        heap = [(0, k)]
        for u, v, w in times:
            graph[u].append((w, v))

        
        while heap:
            weight, curr_node = heapq.heappop(heap)
            
            if weight > cost[curr_node]:
                continue 

            for child_weight, child_node in graph[curr_node]:
                if child_weight + weight < cost[child_node]:
                    cost[child_node] = child_weight + weight
                    heapq.heappush(heap, (child_weight + weight, child_node))

        print(cost)
        for c in cost[1:]:
            if c >= float('inf'):
                return -1
        return max(cost[1:])

