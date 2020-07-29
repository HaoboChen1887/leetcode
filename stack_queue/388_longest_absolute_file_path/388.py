from collections import defaultdict
class Solution:
    # use a map to record the length of each level, because we traverse the dictionary in a dfs manner
    # we won't miss possible longer paths
    def lengthLongestPath(self, input: str) -> int:
        m = defaultdict(int)
        paths = input.split('\n')
        res = 0
        for di in paths:
            depth = di.rfind('\t') + 1
            cur_len = len(di[depth:])
            if di.find('.') != -1:
                res = max(res, m[depth] + cur_len)
            else:
                m[depth + 1] = m[depth] + cur_len + 1
        return res

    # split paths, use number of \t to determine depth
    # if depth less than current depth(denoted by length of stack) pop stack until depth matches
    # if current path is a file, record its length and try to update res
#    def lengthLongestPath(self, input: str) -> int:
#        st = []
#        paths = input.split('\n')
#        res = ''
#        for di in paths:
#            i = 0
#            depth = 1
#            while di[i] == '\t':
#                depth += 1
#                i += 1
#            if depth > len(st):
#                st.append(di[depth - 1:])
#            else:
#                while st and len(st) > depth - 1:
#                    st.pop()
#                st.append(di[depth - 1:])
#            if len(di.split('.')) > 1:
#                new_path = '/'.join(st)
#                if len(new_path) > len(res):
#                    res = new_path
#        return len(res)
