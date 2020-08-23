from collections import defaultdict
class Solution:
    # hashmap record count of each element
    # find the first element with count 1
    def firstUniqChar(self, s: str) -> int:
        res = defaultdict(int)
        for ch in s:
            res[ch] += 1
        for i in range(len(s)):
            if res[s[i]] == 1:
                return i
        return -1
                
            