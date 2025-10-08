class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        count = 0
        fresh_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0
        elif len(queue) == 0:
            return -1
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = {}

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if (r, c) in visited:
                    continue
                visited[(r, c)] = 1
            
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 0:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
            if queue: count += 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return count - 1

