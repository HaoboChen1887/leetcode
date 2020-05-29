class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.helper(res, candidates, 0, target, [])
        return res
        
    def helper(self, res, cand, start, target, tmp):
        if target == 0:
            res.append(sorted(tmp))
        elif target < 0:
            return
        for i in range(start, len(cand)):
            self.helper(res, cand, i, target - cand[i], tmp + [cand[i]])