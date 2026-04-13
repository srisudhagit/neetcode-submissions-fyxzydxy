class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        output = 0
        stack = []
        operators = ["+","-","*","/"]
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                if len(stack) >= 2:
                    operand2 = int(stack.pop())
                    operand1 = int(stack.pop())
                    match token:
                        case "+":
                            result = operand1 + operand2
                        case "-":
                            result = operand1 - operand2
                        case "*":
                            result = operand1 * operand2
                        case _:
                            result = int(operand1 / operand2)
                    stack.append(result)
                else:
                    break
        return int(stack.pop()) if stack else 0
