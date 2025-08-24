class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols = [set() for _ in range(9)]

        for y in range(9):
            row = set()
            for x in range(9):
                if board[y][x] == ".":
                    continue
                if board[y][x] in row:
                    return False
                if board[y][x] in cols[x]:
                    return False
                cols[x].add(board[y][x])
                row.add(board[y][x])
        
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                visited = set()
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        if board[y][x] == ".":
                            continue
                        elif board[y][x] in visited:
                            return False
                        else:
                            visited.add(board[y][x])
        return True