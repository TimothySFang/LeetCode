class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def genParenthesisHelper(parenthesis: str, open:int, closed:int):
            if (open == n and closed == n):
                result.append(parenthesis)
                return
            if (closed < open):
                genParenthesisHelper(parenthesis + ")", open, closed + 1,)
            if (open < n):
                genParenthesisHelper(parenthesis + "(", open + 1, closed, )
        genParenthesisHelper("", 0, 0)
        return result