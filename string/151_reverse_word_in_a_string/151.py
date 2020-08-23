class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()
        return ' '.join(reversed(s))
    
    # NOTE: O(1) method, reverse the entire string then reverse each word, add space when neceesary