class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        p = 1
        pp = 0
        dp = 0
        for i in range(1, len(s) + 1):
            dp = 0 if s[i - 1] == '0' else p
            #if i > 1 and 9 < int(s[i - 2:i]) < 27:
            if i > 1 and (s[i - 2] == '1' or s[i - 2] == '2' and ord(s[i - 1]) < ord('7')):
                dp += pp
            pp = p
            p = dp
        return dp
    
#    def numDecodings(self, s: str) -> int:
#        if not s or s[0] == '0':
#            return 0
#        dp = [0] * (len(s) + 1)
#        dp[0] = 1
#        for i in range(1, len(dp)):
#            dp[i] = 0 if s[i - 1] == '0' else dp[i - 1]
#            if i > 1 and 9 < int(s[i - 2:i]) <= 26:
#                dp[i] += dp[i - 2]
#                
#        return dp[-1]