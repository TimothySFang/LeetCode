class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        characters = {}
        for c in s1:
            if c in characters:
                characters[c] += 1
            else: characters[c] = 1
        
        for i in range(len(s2) - len(s1) + 1):
            windowChars = {}
            for j in range(i, i + len(s1)):
                if s2[j] in windowChars:
                    windowChars[s2[j]] += 1
                else: windowChars[s2[j]] = 1
            if characters == windowChars:
                return True
        return False