class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        i, storeIdx = 0, 0
        s.reverse()
        while i < n:
            j = i
            while j < n and s[j] != ' ':
                j += 1
            print(s[i:j])
            reverseStr(s, i, j - 1)
            i = j + 1

def reverseStr(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1