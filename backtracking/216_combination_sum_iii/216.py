class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        helper(k, 1, n, [], res)
        return res
        
def helper(k, start, n, tmp, res):
    if n < 0:
        return
    if n == 0:
        if len(tmp) == k:
            res.append(tmp)
        return
    
    for i in range(start, 10):
        helper(k, i + 1, n - i, tmp + [i], res)