class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        helper(nums, 0, [], res)
        return res

def helper(nums, level, tmp, res):
    if len(tmp) == len(nums):
        res.append(tmp)
        return
    
    for i in range(level, len(nums)):
        nums[i], nums[level] = nums[level], nums[i]
        helper(nums, level + 1, tmp + [nums[level]], res)
        nums[i], nums[level] = nums[level], nums[i]
        
#    def permute(self, nums: List[int]) -> List[List[int]]:
#        res = []
#        skip = [False] * len(nums)
#        helper(nums, skip, [], res)
#        return res
#        
#def helper(nums, skip, tmp, res):
#    if len(tmp) == len(nums):
#        res.append(tmp)
#        return
#    for i in range(len(nums)):
#        if not skip[i]:
#            skip[i] = True
#            helper(nums, skip, tmp + [nums[i]], res)
#            skip[i] = False