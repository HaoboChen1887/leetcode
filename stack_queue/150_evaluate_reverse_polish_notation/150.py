import math
class Solution:
    # use a stack to track the process. because input is guaranteed to be valid, 
    # when there is an operator we just have to do operations on two numbers before it
    # after the operation, we push the result on to the stack for future record
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set(['+', '-', '*', '/'])
        st = []
        for i in range(len(tokens)):
            if tokens[i] not in ops:
                st.append(tokens[i])
            else:
                y = int(st.pop())
                x = int(st.pop())
                st.append(str(calc(x, tokens[i], y)))
        return st[-1]
                
                
def calc(x, op, y):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        tmp = x / y
        if tmp > 0:
            return math.floor(tmp)
        else:
            return math.ceil(tmp)