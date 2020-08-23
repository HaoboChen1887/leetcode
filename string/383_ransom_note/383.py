from collections import defaultdict
class Solution:
    # hashmap record letter count of magazine
    # decrement count when iterating through ransomNote
    # if a letter is depleted, return false
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = defaultdict(int)
        for ch in magazine:
            m[ch] += 1
        for ch in ransomNote:
            m[ch] -= 1
            if m[ch] < 0:
                return False
        return True