class Solution:
    # 由二维dp方法可知，实际上只需要知道上一轮迭代采用的是哪个颜色，
    # 以及上一轮迭代的最小值和次小值，其他数据均不用记录
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]:
            return 0
        min1, min2 = 0, 0
        idx1 = -1
        for i in range(len(costs)):
            m1, m2 = [sys.maxsize] * 2
            id1 = -1
            for j in range(len(costs[0])):
                cost = costs[i][j] + (min2 if idx1 == j else min1)
                if cost < m1:
                    m2 = m1
                    m1 = cost
                    id1 = j
                elif cost < m2:
                    m2 = cost
            min1, min2, idx1 = m1, m2, id1
        return min1
                
        
    
#    # 取最小值和次小值中合法的那个,避免遍历所有颜色
#    def minCostII(self, costs: List[List[int]]) -> int:
#        if not costs or not costs[0]:
#            return 0
#        n, k = len(costs), len(costs[0])
#        dp = costs
#        curr_min1, curr_min2 = [-1] * 2
#        for i in range(len(dp)):
#            min1, min2 = curr_min1, curr_min2
#            curr_min1, curr_min2 = [-1] * 2
#            for j in range(k):
#                if min1 != j:
#                    dp[i][j] += (0 if min1 < 0 else dp[i - 1][min1])
#                else:
#                    dp[i][j] += (0 if min2 < 0 else dp[i - 1][min2])
#                    
#                if curr_min1 < 0 or dp[i][j] < dp[i][curr_min1]:
#                    curr_min2 = curr_min1
#                    curr_min1 = j
#                elif curr_min2 < 0 or dp[i][j] < dp[i][curr_min2]:
#                    curr_min2 = j
#        return dp[-1][curr_min1]
    
#    def minCostII(self, costs: List[List[int]]) -> int:
#        if not costs or not costs[0]:
#            return 0
#        n, k = len(costs), len(costs[0])
#        dp = [[sys.maxsize] * k for _ in range(n)]
#        for i in range(len((dp[0]))):
#            dp[0][i] = costs[0][i]
#        for i in range(1, len(dp)):
#            for j in range(k):
#                for c in range(k):
#                    if c == j:
#                        continue
#                    dp[i][j] = min(dp[i][j], costs[i][j] + dp[i - 1][c])
#        return min(dp[-1])