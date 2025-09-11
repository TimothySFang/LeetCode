class Solution:
    def isHappy(self, n: int) -> bool:
        def happyChecker(n, visited):
            curr_sum = 0
            for digit in str(n):
                curr_sum += int(digit) * int(digit)

            if curr_sum == 1:
                return True
            elif curr_sum in visited:
                return False
            else:
                visited[curr_sum] = 1
                return happyChecker(curr_sum, visited)
        
        return happyChecker(n, {})