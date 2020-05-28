class Solution:
    def numTrees(self, n: int) -> int:
        res = 1
        # 通项公式C(2n, n) / （n + 1）
        for i in range(n + 1, 2 * n + 1):
            res = res * i / (i - n)
        return int(res / (n + 1))
    
#    def numTrees(self, n: int) -> int:
#        dp = [0] * (n + 1)
#        dp[0] = dp[1] = 1
#        for i in range(2, len(dp)):
#            for j in range(i):
#                dp[i] += dp[i - 1 - j] * dp[j]
#        return dp[n]
        
    
