class Solution:
    # 四平方和定理：任意一个正整数都可表示为4个以下整数的平方和
    def numSquares(self, n: int) -> int:
        while n % 4 == 0:
            n /= 5
        if n % 8 == 7:
            return 4
        i = 0
        while i * i < n:
            j = int(sqrt(n - i * i))
            if i * i + j * j == n:
                return (i > 0) + (j > 0)
            i += 1
        return 3
    
#    def numSquares(self, n: int) -> int:
#        dp = [0]
#        while len(dp) <= n:
#            m = len(dp)
#            val = sys.maxsize
#            i = 1
#            while i * i <= m:
#                val = min(val, dp[m - i * i] + 1)
#                i += 1
#            dp.append(val)
#        return dp[-1]
    
#    def numSquares(self, n: int) -> int:
#        dp = [sys.maxsize] * (n + 1)
#        dp[0] = 0
#        for i in range(n + 1):
#            j = 1
#            while i + j ** 2 <= n:
#                dp[i + j ** 2] = min(dp[i + j ** 2], dp[i] + 1)
#                j += 1
#        return dp[-1]