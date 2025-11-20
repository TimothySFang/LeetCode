class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set()
        def bfs(curr_node):
            queue = deque()
            queue.append(curr_node)            
            while queue:
                curr_node = queue.popleft()
                if curr_node in visited:
                    continue

                visited.add(curr_node)
                if grid[curr_node[0]][curr_node[1]] == "0":
                    continue
                
                for dr, dc in directions:
                    nr, nc = curr_node[0] + dr, curr_node[1] + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        if grid[nr][nc] != "0":
                            queue.append((nr, nc))

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited and grid[r][c] == "1":
                    count += 1
                    bfs((r, c))
        return count