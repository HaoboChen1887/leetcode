from collections import defaultdict
class Solution:
    # use a map to record mapping {pattern:word}
    # recursively check whether each word combination is valid
    # if two pointers reach the end at the same time, there is a match
    # if one one pointer reach the end, the combination is not valid
    # on every interation, we check for a single patter letter
    # starting from where we end last recursion, we try all possible word combinations
    # if the word has already been mapped with some pattern letter, we move forward to the next recursion
    # if not, we check if it is taken by other pattern letters
    #       if yes, we continue to try the next word
    #       if not, we add it to map and move forward to the next recursion
    #       if then the recursion gives false, we need to remove the word from the map
    def wordPatternMatch(self, pattern: str, str: str) -> bool:
        m = defaultdict(int)
        return helper(pattern, 0, str, 0, m)
    
def helper(pattern, p, str, r, m):
    if p == len(pattern) and r == len(str):
        return True
    if p == len(pattern) or r == len(str):
        return False
    c = pattern[p]
    for i in range(r, len(str)):
        t = str[r : i + 1]
        if c in m and m[c] == t:
            if helper(pattern, p + 1, str, i + 1, m):
                return True
        elif c not in m:
            if t in m.values():
                continue
            else:
                m[c] = t
                if helper(pattern, p + 1, str, i + 1, m):
                    return True
                m.pop(c)
    return False