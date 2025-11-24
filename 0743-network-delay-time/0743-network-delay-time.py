class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        cost = [float('inf')] * (n + 1) # cost array at n + 1 length because nodes go from 1 to n
        cost[k] = 0
        heap = [(0, k)] # heap for graph traversal where each value is (cost, node) 

        while heap:
            weight, curr_node = heapq.heappop(heap)

            if weight > cost[curr_node]:
                # reduce looping if this one is already the "heavier path"
                continue

            for v, w in graph[curr_node]:
                # looping through all the neighbor nodes of curr_node

                if w + weight < cost[v]:
                    # this path is shorter
                    cost[v] = w + weight
                    heapq.heappush(heap, (w + weight, v))
        print(cost)
        for i in range(1, len(cost)):
            if cost[i] >= float('inf'):
                return -1
    
        return max(cost[1:])



