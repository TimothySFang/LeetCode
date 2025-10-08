class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        number_dict = {"1":"", "2":"abc", "3":"def", "4":"ghi", "5":"jkl","6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        result = []

        ans_length = 0
        for d in digits:
            if d != "1":
                ans_length += 1

        def backtracking(path, i):
            if len(path) == ans_length:
                result.append(path)
                return

            digit = digits[i]
            for alpha in number_dict[digit]:
                backtracking(path + alpha, i + 1)

        backtracking("", 0)
        return result