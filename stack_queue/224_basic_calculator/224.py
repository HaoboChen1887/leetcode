class Solution:
    # use a stack to keep track of nested brackets
    # if encounter '+' or '-' we add the previous number with correct sign to res
    #   reset num
    # if encounter number, we increment num until we reach an operator
    # if encounter '(', we push the results we get so far and the sign onto stack
    #   reset sign and res for calculating values inside the bracket
    # if encounter ')', we add the last number in the bracket with correct sign
    #   reset num
    #   then modify with the correct sign according to the sign we pushed onto the stack
    #   and add the results before going into the bracket
    # if the final char is not ')', we need to add the final number
    def calculate(self, s: str) -> int:
        res = 0
        st = []
        sign = 1
        num = 0
        for i in range(len(s)):
            if s[i] in string.digits:
                num = 10 * num + int(s[i])
            elif s[i] == '+' or s[i] == '-':
                res += sign * num
                num = 0
                sign = 1 if s[i] == '+' else -1
            elif s[i] == '(':
                st.append(res)
                st.append(sign)
                res = 0
                sign = 1
            elif s[i] == ')':
                res += sign * num
                num = 0
                res *= st.pop()
                res += st.pop()
        res += sign * num
        return res
                