class Solution:
    # two pointer brute-force
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        m, n = len(haystack), len(needle)
        if m < n:
            return -1
        for i in range(m - n + 1):
            j = 0
            while j < n:
                if haystack[i + j] != needle[j]:
                    break
                j += 1
            if j == n:
                return i
        return -1