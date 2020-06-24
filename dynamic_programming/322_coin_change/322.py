class Solution:
    res = sys.maxsize
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        coins.sort()
        self.helper(coins, n - 1, amount, 0)
        if self.res == sys.maxsize:
            return -1
        return self.res
        
    def helper(self, coins, start, target, cur):
        if start < 0:
            return
        if target % coins[start] == 0:
            self.res = min(self.res, cur + target // coins[start])
            return
        for i in range(target // coins[start], -1, -1):
            if cur + i >= self.res - 1:
                break
            self.helper(coins, start - 1, target - i * coins[start], cur + i)
            
#    def coinChange(self, coins: List[int], amount: int) -> int:
#        memo = [sys.maxsize] * (amount + 1)
#        memo[0] = 0
#        return helper(memo, coins, amount)
#    
#def helper(memo, coins, target):
#    if target < 0:
#        return -1
#    if memo[target] != sys.maxsize:
#        return memo[target]
#    for c in coins:
#        tmp = helper(memo, coins, target - c)
#        if tmp >= 0:
#            memo[target] = min(memo[target], tmp + 1)
#    if memo[target] == sys.maxsize:
#        return -1
#    return memo[target]
    
#    def coinChange(self, coins: List[int], amount: int) -> int:
#        dp = [amount + 1] * (amount + 1)
#        dp[0] = 0
#        for i in range(1, len(dp)):
#            for c in coins:
#                if i - c >= 0:
#                    dp[i] = min(dp[i], dp[i - c] + 1)
#        if dp[-1] == amount + 1:
#            return -1
#        return dp[-1]