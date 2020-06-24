class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(len(dp)):
            dp[i][0] = i
        for i in range(len(dp[0])):
            dp[0][i] = i
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min([dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]])
        return dp[-1][-1]
        
#    def minDistance(self, word1: str, word2: str) -> int:
#        m = len(word1)
#        n = len(word2)
#        memo = [[0] * n for _ in range(m)]
#        return helper(word1, 0, word2, 0, memo)
#        
#def helper(word1, i, word2, j, memo):
#    # 如果word1达到长度，剩下的操作均为插入或删除，长度为剩余的word2长度
#    if i == len(word1):
#        return len(word2) - j
#    # 同上
#    if j == len(word2):
#        return len(word1) - i
#    if memo[i][j] > 0:
#        return memo[i][j]
#    res = 0
#    # 如果两个单词当前位置相同，无需任何操作，不计数，跳过并进入下一个字母比较
#    if word1[i] == word2[j]:
#        return helper(word1, i + 1, word2, j + 1, memo)
#    else:
#        # 分别比较当前操作是插入，删除，替换时的计数
#        # 在word1的i位置插入对应的字母，相当于word1比较位置不变，word2向前进一位
#        insert_cnt = helper(word1, i, word2, j + 1, memo)
#        # 将word1的i位置删除，相当于word1向前进一位，word2比较位置不变
#        delete_cnt = helper(word1, i + 1, word2, j, memo)
#        # 将word1的i位置替换为对应字母，相当于两字母相同，
#        # 但由于经过操作所以需要计数，两单词同时向前进一位
#        replace_cnt = helper(word1, i + 1, word2, j + 1, memo)
#        res = min([insert_cnt, delete_cnt, replace_cnt]) + 1
#    memo[i][j] = res
#    return res