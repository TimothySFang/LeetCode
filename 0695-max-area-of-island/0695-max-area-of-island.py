class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        visited = {}

        def dfs(y, x):
            if (y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0]) or (y, x) in visited or grid[y][x] == 0):
                return 0
            
            visited[(y, x)] = 1
            return 1 + dfs(y + 1, x) + dfs(y - 1, x) + dfs(y, x + 1) + dfs(y, x - 1)
            
        max_area = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                max_area = max(max_area, dfs(y, x))
                
        return max_area
        