class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dp[i][j] is the minimum worstcase cost for number between [i,j]
        # 这题主旨是求最小的最大值，
        # 最后求出的情况是每次都用最优的猜法猜但是每次都遇到最差的情况的解
        # 两个基本情况是：
        #	1个数： cost为0，因为直接猜中没有cost
        #	2个数： cost为较小的那个，因为即使没猜中这也是最优的猜法，由此才能的出需要的能保证完成比赛最少的钱
        # 之后的情况可由上述两种情况导出
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for l in range(n - 1, 0, -1):
            for r in range(l + 1, n + 1):
                dp[l][r] = min(i + max(dp[l][i - 1], dp[i + 1][r]) for i in range(l, r))
            print(dp)
        return dp[1][n]