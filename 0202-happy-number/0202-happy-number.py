from collections import defaultdict
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        

        while n not in visited:
            visited.add(n)
            n = self.getSumSquares(n)
            if n == 1:
                return True
        
        return False

    def getSumSquares(self, n):
        accumulator = 0
        print(n)
        while n:
            digit = n % 10
            digit = digit ** 2
            accumulator += digit
            n = n // 10
        return accumulator

            