class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = set()
        rows, cols = len(grid), len(grid[0])
        count = 0

        def bfs(r, c):
            queue = collections.deque()
            queue.append((r, c))
            visited.add((r, c))
            while queue:
                row, col = queue.pop()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    new_r, new_c = row + dr, col + dc
                    if new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] == "1" and (new_r, new_c) not in visited:
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))
                    

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    count += 1

        return count
                    