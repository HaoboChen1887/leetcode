class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        helper(nums, 0, [], res)
        return res

def helper(nums, level, tmp, res):
    if len(tmp) == len(nums):
        res.append(tmp)
        return
    
    for i in range(level, len(nums)):
        # 每次循环前往前找是否有重复用过的数字，由于数组排过序，如果没有重复的j一定等于level - 1
        j = i - 1
        while j >= level and nums[j] != nums[i]:
            j -= 1
        if j != level - 1:
            continue
        nums[i], nums[level] = nums[level], nums[i]
        helper(nums, level + 1, tmp + [nums[level]], res)
        nums[i], nums[level] = nums[level], nums[i]
        
#    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#        nums.sort()
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
#        if skip[i]:
#            continue
#        if i > 0 and nums[i] == nums[i - 1] and not skip[i - 1]:
#            continue
#        skip[i] = True
#        helper(nums, skip, tmp + [nums[i]], res)
#        skip[i] = False