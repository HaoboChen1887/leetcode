class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        if n == 1:
            return []
        helper(n, 2, [], res)
        return res
    
def helper(n, start, tmp, res):
    if len(tmp) > 0:
        res.append(tmp + [n])
    # 此处边界不能用ceil，因为会有整除的情况，此时range上界仍然需要加1
    for i in range(start, int(sqrt(n)) + 1):
        if n % i == 0:
            helper(n // i, i, tmp + [i], res)
    
#def helper(n, start, tmp, res):
#    print(n, tmp)
#    if n == 1:
#        if len(tmp) > 1:
#            res.append(tmp)
#        return
#    for i in range(start, n + 1):
#        if n % i == 0:
#            helper(n // i, i, tmp + [i], res)