class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c_dict = {}
        t_dict = {}
        for c in s:
            if c in c_dict:
                c_dict[c] +=1
            else:
                c_dict[c] = 1
        for c in t:
            if c in t_dict:
                t_dict[c] += 1
            else:
                t_dict[c] = 1
        return c_dict == t_dict