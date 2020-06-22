class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for k in range(len(nums) - 2):
            if nums[k] > 0:
                break
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            target = 0 - nums[k]
            i, j = k + 1, len(nums) - 1
            while i < j:
                if nums[i] + nums[j] == target:
                    res.append([nums[k], nums[i], nums[j]])
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] > target:
                    j -= 1
                else:
                    i += 1
        return res
            
            
# ************************** TLE ***********************************
#    def threeSum(self, nums: List[int]) -> List[List[int]]:
#        nums.sort()
#        print(nums)
#        res = []
#        helper(nums, 0, 0, [], res)
#        return res
#        
#def helper(nums, start, remain, tmp, res):
#    if len(tmp) > 3:
#        return
#    if len(tmp) == 3 and remain == 0:
#        res.append(tmp)
#        return
#    for i in range(start, len(nums)):
#        if i > start and nums[i] == nums[i - 1]:
#            continue
#        helper(nums, i + 1, remain - nums[i], tmp + [nums[i]], res)
        
        