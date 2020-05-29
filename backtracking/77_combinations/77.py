class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        tmp = [0] * k
        i = 0
        while i >= 0:
            tmp[i] += 1
            if tmp[i] > n:
                i -= 1
            elif i == k - 1:
                res.append(tmp[:])
            else:
                i += 1
                tmp[i] = tmp[i - 1]
        return res

#    res = []
#    def combine(self, n: int, k: int) -> List[List[int]]:
#        if k < 0 or k > n:
#            return []
#        if k == 0:
#            return [[]]
#        self.res = self.combine(n - 1, k - 1)
#        for path in self.res:
#            path.append(n)
#        self.res += self.combine(n - 1, k)
#        return self.res
    
#    def combine(self, n: int, k: int) -> List[List[int]]:
#        if k > n or k < 0:
#            return []
#        res = []
#        dfs(1, n, k, [], res)
#        return res
#        
#def dfs(i, n, k, tmp, res):
#    if len(tmp) == k:
#        res.append(tmp)
#        return
#    for new in range(i, n + 1):
#        dfs(new + 1, n, k, tmp + [new], res)