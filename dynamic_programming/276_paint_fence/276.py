class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        same, diff = 0, k
        for i in range(2, n + 1):
            t = diff
            diff = (same + diff) * (k - 1)
            same = t
        return same + diff
    
#    def numWays(self, n: int, k: int) -> int:
#        if k <= 0 or n <= 0:
#            return 0
#        dp = [0] * (n + 1)
#        dp[1] = k
#        for i in range(2, n + 1):
#            dp[i] = (dp[i - 1] + dp[i - 2]) * (k - 1)
#        return dp[-1] + dp[-2]