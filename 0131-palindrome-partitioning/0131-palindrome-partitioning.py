class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def isPalindrome(string):
            return string == string[::-1]

        def backtracking(start, path):
            if start == (len(s)):
                result.append(path.copy())
                return True

            for end in range(start, len(s)):
                substring = s[start:end + 1]
                if isPalindrome(substring):
                    path.append(substring)
                    backtracking(end + 1, path)
                    path.pop()

        backtracking(0, [])
        return result