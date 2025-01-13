class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_visited = {}
        t_visited = {}
        for char in s:
            if char in s_visited:
                s_visited[char] += 1
            else:
                s_visited[char] = 1
        for char in t:
            if char in t_visited:
                t_visited[char] += 1
            else:
                t_visited[char] = 1

        if s_visited == t_visited:
            return True
        else: return False
        