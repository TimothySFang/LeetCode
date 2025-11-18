class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        directions = [(0, -1), (-1, 0), (1, 0), (0, 1)]

        def bfs(r, c):
            if (r, c) in visited:
                return
            
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "1":
                    bfs(nr, nc)



        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    count += 1
        
        return count