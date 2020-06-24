class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        dp = [sys.maxsize] * len(grid[0])
        dp[0] = 0
        for i in range(len(grid)):
            for j in range(len(dp)):
                if j == 0:
                    dp[j] += grid[i][j]
                else:
                    dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]
        return dp[-1]
    
#    def minPathSum(self, grid: List[List[int]]) -> int:
#        if not grid or not grid[0]:
#            return -1
#        dp = grid
#        for i in range(len(dp)):
#            for j in range(len(dp[0])):
#                if i == 0:
#                    dp[i][j] += 0 if j == 0 else dp[i][j - 1]
#                elif j == 0:
#                    dp[i][j] += dp[i - 1][j]
#                else:
#                    dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])
#        return dp[-1][-1]
                    