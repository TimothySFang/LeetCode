class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_size = 0

        def dfs(y, x):
            if not (0 <= y < len(grid) and 0 <= x < len(grid[0])):
                return 0
            if grid[y][x] != 1 or (y, x) in visited:
                return 0
                
            visited.add((y, x))
            
            return (1 + dfs(y + 1, x) + dfs(y - 1, x) + dfs(y, x + 1) + dfs(y, x - 1))


        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if (y, x) not in visited and grid[y][x] == 1:
                    max_size = max(max_size, dfs(y, x))
        return max_size

