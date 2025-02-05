class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = []
        for c in s:
            if c.isalnum():
                new_string.append(c.lower())
        traverse_range = len(new_string) // 2
        string_length = len(new_string)
        for index in range(traverse_range):
            right_index = string_length - 1 - index
            if (new_string[index] != new_string[right_index]):
                return False
        return True