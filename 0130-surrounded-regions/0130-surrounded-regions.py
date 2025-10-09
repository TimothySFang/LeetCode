class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        stack = deque()
        rows, cols = len(board), len(board[0])
        visited = set()
        def bfs(node):
            print(node)
            stack = deque()
            stack.append(node)

            while stack:
                r, c = stack.popleft()
                if (r, c) in visited:
                    continue

                visited.add((r, c))
                directions = ((1,0), (0, 1), (-1, 0), (0, -1))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows) and (0 <= nc < cols) and board[nr][nc] == "O":
                        stack.append((nr, nc))


        for r in range(rows):
            if board[r][0] == "O":
                bfs((r, 0))
            if board[r][cols - 1] == "O":
                bfs((r, cols - 1))

        for c in range(cols):
            if board[0][c] == "O":
                bfs((0, c))
            if board[rows - 1][c] == "O":
                bfs((rows - 1, c))
                
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"