class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        bracket_pairs = {"(": ")", "{": "}", "[": "]"}
        for c in s:
            if c in bracket_pairs:
                queue.append(c)
            else:
                if len(queue) <= 0 or c != bracket_pairs[queue.pop()]:
                    return False

        return len(queue) == 0