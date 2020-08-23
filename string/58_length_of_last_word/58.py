class Solution:
    # starting from the end of string, skip spaces and count the len of the first word encountered
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        right = len(s) - 1
        while right >= 0 and s[right] == ' ':
            right -= 1
        while right >= 0 and s[right] != ' ':
            right -= 1
            res += 1
        return res