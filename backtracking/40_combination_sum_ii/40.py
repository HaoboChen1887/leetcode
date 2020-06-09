class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        helper(candidates, 0, target, res, [])
        return res
        
        
        
def helper(candidates, idx, target, res, tmp):
    if target < 0:
        return
    if target == 0:
        res.append(tmp)
        return
    
    for i in range(idx, len(candidates)):
        if i > idx and candidates[i] == candidates[i - 1]:
            continue
        helper(candidates, i + 1, target - candidates[i], res, tmp + [candidates[i]])
        