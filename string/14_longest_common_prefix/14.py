class Solution:
    # sort the list. Because of how words is ordered alphabatically 
    # if there is a common prefix, it has to be in both the head and tail of the list
    # additionally, in cases like ['flower', 'flow', 'flower']
    # after sort, it will become ['flow', 'flower', 'flower'] and causes no problem
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        strs.sort()
        n = min(len(strs[0]), len(strs[-1]))
        i = 0
        while i < n and strs[0][i] == strs[-1][i]:
            i += 1
        return strs[0][:i]
            
            