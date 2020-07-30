import math
class Solution:
    # initialize op to '+' to handle the first number
    # if encounter number, record it
    # if encounter an operator or reach the end of the string, do the following
    #   if encounter '+' or '-' push current number with correct sign onto stack
    #   if encounter '*' or '/' pop one number from stack and do according operation
    # after handling all '*' and '/', summing the stack up gives the result
    def calculate(self, s: str) -> int:
        st = []
        op = '+'
        num = 0
        for i in range(len(s)):
            if s[i] in string.digits:
                num = num * 10 + int(s[i])
            if s[i] == '+' or s[i] == '-' or s[i] == '/' or s[i] == '*' or i == len(s) - 1:
                if op == '+':
                    st.append(num)
                elif op == '-':
                    st.append(-num)
                elif op == '*':
                    st.append(st.pop() * num)
                elif op == '/':
                    st.append(int(st.pop() / num))
                op = s[i]
                num = 0
        return sum(st)
                