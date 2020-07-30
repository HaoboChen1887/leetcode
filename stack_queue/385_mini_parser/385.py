class Solution:
    # if s is empty we can return it
    # if s doesn't start with a '[', then it only contains an integer and we can return it
    # we track the nested brackets with a stack
    # we record the start index of each number with start
    # if we encounter a '[' it means there needs to be a new NestedInteger object
    #   so we push it to the stack and increment start to skip '['
    # if we encounter ',' or ']'
    #   if ',' the i > start always hold, and we add the number to the top object on the stack
    #   if ']', we check whether i > start to determine whether it is the first ']' we encounter in a row
    #   in either cases, we add the number to the top object on the stack
    # then we increment start to skip the current ',' or ']'
    # if we encounter a ']', it means this is the end of a NestedInteger object
    #   since we have already added numbers to such object
    #   we can pop it off the stack 
    #   and add it to the next top object on the stack if stack size > 1
    # in the end the stack contains only one object, which is the answer
    
    def deserialize(self, s: str) -> NestedInteger:
        if not s:
            return NestedInteger()
        if s[0] != '[':
            return NestedInteger(int(s))
        st = []
        start = 1
        for i in range(len(s)):
            if s[i] == '[':
                st.append(NestedInteger())
                start = i + 1
            elif s[i] == ',' or s[i] == ']':
                if i > start:
                    st[-1].add(NestedInteger(int(s[start:i])))
                start = i + 1
                if s[i] == ']':
                    if len(st) > 1:
                        t = st.pop()
                        st[-1].add(t)
        return st[-1]
