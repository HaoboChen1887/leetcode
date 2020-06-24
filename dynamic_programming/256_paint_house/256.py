class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]:
            return 0
        dp = [[0] * 3 for _ in range(len(costs))]
        for i in range(len((dp[0]))):
            dp[0][i] = costs[0][i]
        for i in range(1, len(dp)):
            for j in range(3):
                dp[i][j] = costs[i][j] + min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3])
        return min(dp[-1])