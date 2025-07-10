class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis_set = { '(': ')', '[':']', '{':'}'}
        stack = []
        for p in s:
            if p in parenthesis_set:
                stack.append(parenthesis_set[p])
            elif len(stack) == 0 or stack.pop() != p:
                return False
        return len(stack) == 0