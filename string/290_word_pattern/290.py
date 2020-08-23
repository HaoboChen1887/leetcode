from collections import defaultdict
class Solution:
    # use two map to store the last index where each letter/word appears and check on-the-fly
    # if there is a mismatch return false
    def wordPattern(self, pattern: str, str: str) -> bool:
        str = str.strip().split()
        if len(str) != len(pattern):
            return False
        m1, m2 = defaultdict(int), defaultdict(int)
        for i in range(len(pattern)):
            if m1[pattern[i]] != m2[str[i]]:
                return False
            m1[pattern[i]] = i + 1
            m2[str[i]] = i + 1
        return True
