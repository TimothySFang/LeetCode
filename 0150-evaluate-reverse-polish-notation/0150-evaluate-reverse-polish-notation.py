class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        for t in tokens:
            if t in operators:
                # calculate
                val_a = stack.pop()
                val_b = stack.pop()
                if t == "+":
                    stack.append(val_a + val_b)
                elif t == "-":
                    stack.append(val_b - val_a)
                elif t == "/":
                    stack.append(int(val_b / val_a))  
                elif t == "*":
                    stack.append(val_a * val_b)
            else:
                stack.append(int(t))
        return stack[0]
