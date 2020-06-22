class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n + 1)
        return helper(n, memo)

def helper(n, memo):
    if n <= 1:
        return 1
    if memo[n] > 0:
        return memo[n]
    memo[n] = helper(n - 1, memo) + helper(n - 2, memo)
    return memo[n]

#    def climbStairs(self, n: int) -> int:
#        if n < 3:
#            return n
#        a = 1
#        b = 2
#        for i in range(2, n):
#            b += a
#            a = b - a
#        return b
            
#    def climbStairs(self, n: int) -> int:
#        if n < 2:
#            return 1
#        dp = [0] * n
#        dp[0] = 1
#        dp[1] = 2
#        for i in range(2, n):
#            dp[i] = dp[i - 1] + dp[i - 2]
#        return dp[-1]