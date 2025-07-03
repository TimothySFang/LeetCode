class Solution:
    def isPalindrome(self, s: str) -> bool:
        st, ed = 0, len(s) -1
        while ed > st:
            if not s[st].isalnum():
                st += 1
            elif not s[ed].isalnum():
                ed -= 1
            elif s[st].lower() == s[ed].lower():
                st += 1
                ed -= 1
            else:
                return False
        return True
