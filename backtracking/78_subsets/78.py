class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for bit in range(0, 1 << len(nums)):
            tmp = helper(nums, bit)
            res.append(tmp)
        return res
        
def helper(nums, bit):
    tmp = []
    idx = 0
    while bit > 0:
        if bit & 1:
            tmp.append(nums[idx])
        bit >>= 1
        idx += 1
    return tmp

#    def subsets(self, nums: List[int]) -> List[List[int]]:
#        res = []
#        tmp = []
#        helper(0, tmp, res, sorted(nums))
#        return res
#    
#def helper(idx, tmp, res, nums):
#    if idx == len(nums):
#        res.append(tmp)
#        return
#    helper(idx + 1, tmp + [nums[idx]], res, nums)
#    helper(idx + 1, tmp, res, nums)
    
#    def subsets(self, nums: List[int]) -> List[List[int]]:
#        nums.sort()
#        res = [[]]
#        for num in nums:
#            res += [item + [num] for item in res]
#        return res
            
        