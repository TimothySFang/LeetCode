class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        visited = {}
        for i in range(len(s)):
            if s[i] in visited:
                visited[s[i]] += 1
            else : 
                visited[s[i]] = 1
        
        for i in range(len(s)):
            if visited[s[i]] == 1:
                return i
        return - 1