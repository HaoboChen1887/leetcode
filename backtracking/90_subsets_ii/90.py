class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.helper(nums, 0, [], res)
        return res
        
    def helper(self, nums, idx, path, res):
        res.append(path)
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            self.helper(nums, i + 1, path + [nums[i]], res)
    
#    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#        nums.sort()
#        res = [[]]
#        last = None
#        new_add = 0
#        for idx in range(len(nums)):
#            tmp = []
#            if last == nums[idx]:
#                for i in range(len(res) - new_add, len(res)):
#                    tmp.append(res[i] + [nums[idx]])
#            else:
#                for item in res:
#                    tmp.append(item + [nums[idx]])
#            new_add = len(tmp)
#            res += tmp
#            last = nums[idx]
#        return res
    
#    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#        res = []
#        nums.sort()
#        for bit in range(1 << len(nums)):
#            tmp = helper(bit, nums, res)
#            if tmp not in res:
#                res.append(tmp)
#        return res
#        
#def helper(bit, nums, res):
#    tmp = []
#    idx = 0
#    while bit > 0:
#        if bit & 1:
#            tmp.append(nums[idx])
#        idx += 1
#        bit >>= 1
#    return tmp