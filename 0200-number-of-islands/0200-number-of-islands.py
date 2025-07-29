class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        island_count = 0
        def bfs(y, x):
            if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
                return
            if (y, x) in visited:
                return
            else: 
                visited.add((y, x))

            if grid[y][x] == "1":
                bfs(y + 1, x)
                bfs(y - 1, x)
                bfs(y, x + 1)
                bfs(y, x - 1)
        
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if (y, x) in visited:
                    continue
                elif grid[y][x] == "1":
                    island_count += 1
                    bfs(y, x)
                else:
                    visited.add((y, x))
        return island_count