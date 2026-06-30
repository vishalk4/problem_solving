from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in "+-*/": # if t is an operator
                # pop the top two elements from the stack
                b = stack.pop()
                a = stack.pop() # second popped element is the first operand
                # perform the corresponding operation
                if t == "+":
                    result = a + b
                elif t == "-":
                    result = a - b
                elif t == "*":
                    result = a * b
                else:
                    result = int(a / b) # Use int(a / b) to round off toward zero
                stack.append(result) # push the result back onto the stack
            else:
                # if the t is a number, convert it to int and push to stack
                stack.append(int(t))
        return stack[-1]
