class Solution:
    # this problem only ask for possible state after ONE move
    # brute force
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        res = []
        for i in range(1, len(s)):
            if s[i] == '+' and s[i - 1] == '+':
                res.append(s[:i - 1] + '--' + s[i + 1:])
        return res
        