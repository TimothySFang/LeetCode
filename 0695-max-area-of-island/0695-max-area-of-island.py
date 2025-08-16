class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_size = 0
        H, W = len(grid), len(grid[0])

        def bfs(y, x):
            # out of bounds or water or already seen
            if not (0 <= y < H and 0 <= x < W): 
                return 0
            if grid[y][x] != 1 or (y, x) in visited:
                return 0

            visited.add((y, x))
            # count this cell + neighbors
            return (
                1
                + bfs(y + 1, x)
                + bfs(y - 1, x)
                + bfs(y, x + 1)
                + bfs(y, x - 1)
            )

        for y in range(H):
            for x in range(W):
                if (y, x) not in visited and grid[y][x] == 1:
                    max_size = max(max_size, bfs(y, x))

        return max_size
