class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim's implementation

        def manhattanDistance(p1, p2):
            return (abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]))


        heap = [(0, points[0][0], points[0][1])]
        visited = set()
        cost = 0

        while heap:
            if len(visited) == len(points):
                return cost

            weight, x, y = heapq.heappop(heap)

            if (x, y) in visited:
                continue
            
            visited.add((x, y))
            print((x, y))
            cost += weight
            
            for nx, ny in points:
                if (nx, ny) in visited:
                    continue
                # calc manhattan distance and update heap
                node_cost = manhattanDistance((nx, ny), (x, y))
                heapq.heappush(heap, (node_cost, nx, ny))

        return cost

