class Solution:
    # the problem asks if the starting player can guarantee a win
    # which is equal to asking whehter there is at least one way player one can win
    # this is equal to asking is it possible to guarantee that player 2 can not win no matter what
    # by following this logic, we construct the recursion
    def canWin(self, s: str) -> bool:
        for i in range(1, len(s)):
            if s[i] == '+' and s[i - 1] == '+' and not self.canWin(s[:i - 1] + '--' + s[i + 1:]):
                return True
        return False
        