class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = set(wordDict)
        dp = [False] * (len(s) + 1)
        # dp[i]表示s[0:i]是否可被拆分并匹配字典
        dp[0] = True
        for i in range(len(dp)):
            for j in range(i):
                if dp[j] and s[j:i] in dic:
                    dp[i] = True
                    break
            print(dp)
        return dp[-1]
        
#    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#        dic = set(wordDict)
#        memo = [-1] * len(s)
#        return helper(s, dic, 0, memo)
#        
#   memo[i]表示下标为[i:n]的子字符串是否可被拆分并匹配字典
#
#def helper(s, dic, pos, memo):
#    if pos >= len(s):
#        return True
#    if memo[pos] != -1:
#        return memo[pos]
#    for i in range(pos + 1, len(s) + 1):
#        if s[pos:i] in dic and helper(s, dic, i, memo):
#            memo[pos] = 1
#            return memo[pos]
#    memo[pos] = 0
#    return memo[pos]
#        