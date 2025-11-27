class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        # andy's solution
        adj = [[] for _ in range(n)]
        for frm, to, price in flights:
            adj[frm].append((to, price))

        priority_queue = [(0, src, 0)]  # (cost, cur_node, stops_left_to_take)
        steps = [math.inf] * n

        while priority_queue:
            cost, cur_node, steps_taken = heapq.heappop(priority_queue)
            
            if steps_taken >= steps[cur_node]:
                continue
            if steps_taken > k + 1:
                continue
            if cur_node == dst:
                return cost

            steps[cur_node] = steps_taken

            for next_node, flight_cost in adj[cur_node]:
                heapq.heappush(priority_queue, (cost + flight_cost, next_node, steps_taken + 1))

        return -1