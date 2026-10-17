
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # ["-203,"5","+"]

        operands = []

        # while not op_stack:
            # op_stack.pop()
        op = {
            '+':lambda x, y: x+y,
            '-':lambda x, y: x-y,
            '*':lambda x, y: x*y,
            '/':lambda x, y: int(x/y),
        }

        
        for i, token in enumerate(tokens):
            if token in op:
                op1 = operands.pop()  # Remove int() conversion here
                op2 = operands.pop() 
                result = op[token](op2,op1)
                operands.append(result)
            # operand 
            else:
                operands.append(int(token))

        return operands.pop()