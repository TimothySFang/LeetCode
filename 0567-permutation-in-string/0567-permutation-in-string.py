class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        curr_string = [0] * 26
        s1_array = [0] * 26

        # populate the left most curr window and s1_array
        for i in range(len(s1)):
            s1_array[ord(s1[i]) - ord('a')] += 1
            curr_string[ord(s2[i]) - ord('a')] += 1
        
        l, r = 0, len(s1)
        if curr_string == s1_array:
            return True
        while r < len(s2):
            curr_string[ord(s2[l]) - ord('a')] -= 1
            curr_string[ord(s2[r]) - ord('a')] += 1
            l += 1
            r += 1

            if curr_string == s1_array:
                return True
        return False