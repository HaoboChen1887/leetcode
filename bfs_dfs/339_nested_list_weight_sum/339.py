class Solution:
    # dfs
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        res = 0
        for nInt in nestedList:
            res += dfs(nInt, 1)
        return res
            
def dfs(nInt, depth):
    if nInt.isInteger():
        return nInt.getInteger() * depth
    res = 0
    for item in nInt.getList():
        res += dfs(item, depth + 1)
    return res