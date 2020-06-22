class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []
        helper(word, 0, res)
        return res
    
def helper(word, pos, res):
    res.append(word)
    for i in range(pos, len(word)):
        j = 1
        while i + j <= len(word):
            helper(word[:i] + str(j) + word[i + j:], i + len(str(j)) + 1, res)
            j += 1
            
#    def generateAbbreviations(self, word: str) -> List[str]:
#        if len(word) == 0:
#            return [""]
#        res = []
#        for bit in range(2 ** len(word)):
#            cnt = 0
#            tmp = ""
#            for i in range(len(word)):
#                if bit & 1:
#                    cnt += 1
#                    if i == len(word) - 1:
#                        tmp += str(cnt)
#                else:
#                    if cnt != 0:
#                        tmp += str(cnt)
#                        cnt = 0
#                    tmp += word[i]
#                bit >>= 1
#            res.append(tmp)
#        return set(res)
            
