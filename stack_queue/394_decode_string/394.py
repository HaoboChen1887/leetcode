class Solution:
    # use 2 stacks to store the status of decoding
    # s_num stores number of times to repeat
    # s_str stores the string to repeat
    # scan over the string
    # if encounter a letter, store the letter in t
    # if encounter a number, add the number to counter (note that the number may be more than one digit)
    # if encounter '[', push the recorded string on to string stack and counter onto counter stack
    #   clear the counter and string recorder
    # if encounter ']', pop off the most recent counter
    #   repeatedly add t to the end of string counter's top element, to handle cases of nested brackets
    #   pop off the top element from string stack
    # after the loop if the stack is not empty, the last char is not ']', stack top is the answer
    # if the stack is empty, then the top element has already been poped of the stack
    # and t stores the answer
    def decodeString(self, s: str) -> str:
        t = ''
        s_num = []
        s_str = []
        cnt = 0
        for i in range(len(s)):
            if s[i] in string.digits:
                cnt = 10 * cnt + int(s[i])
            elif s[i] == '[':
                s_num.append(cnt)
                s_str.append(t)
                cnt = 0
                t = ''
            elif s[i] == ']':
                k = s_num.pop()
                for i in range(k):
                    s_str[-1] += t
                t = s_str.pop()
            else:
                t += s[i]
        return t if not s_str else s_str[-1]