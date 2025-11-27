class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # djikstra's with edge_count
        # utilize min-heap to ensure the first time we find the solution, its the cheapest.

        graph = defaultdict(list)
        steps = [float('inf')] * (n)
        heap = [(0, src, 0)]
        # steps[src] = 0

        for fro, to, price in flights:
            graph[fro].append((price, to))

        while heap:
            weight, curr_node, edge_count = heapq.heappop(heap)
            
            if edge_count > k + 1:
                continue
            
            if edge_count >= steps[curr_node]:
                continue # essentially, if we have reached the current node in the past, it will always have been cheaper...

            if curr_node == dst:
                return weight

            steps[curr_node] = edge_count

            for new_cost, new_node in graph[curr_node]:
                cost = new_cost + weight
                heapq.heappush(heap, (cost, new_node, edge_count + 1))
                
        return -1
