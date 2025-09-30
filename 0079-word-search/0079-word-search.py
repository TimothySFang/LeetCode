class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        def backtrack(i, r, c):
            if i == len(word):
                return True
            
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[i]):
                return False

            temp = board[r][c]
            board[r][c] = "temp"
            res = backtrack(i + 1, r + 1, c) or backtrack(i + 1, r - 1, c) or backtrack(i + 1, r, c + 1) or backtrack(i + 1, r, c - 1)
            
            board[r][c] = temp
            return res
        for y in range(cols):
            for x in range(rows):
                if backtrack(0, x, y):
                    return True
        return False


