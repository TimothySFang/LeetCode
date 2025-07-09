class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        curr_str = {}
        curr_max = 0
        while r < len(s):
            while s[r] in curr_str:
                curr_str.pop(s[l])
                l += 1
            curr_str[s[r]] = 1
            
            if r - l + 1> curr_max:
                curr_max = r - l + 1
            r += 1
        return curr_max