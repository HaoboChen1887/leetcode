class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2
        j = n - 1
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
                
        i += 1
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
                
#    def nextPermutation(self, nums: List[int]) -> None:
#        """
#        Do not return anything, modify nums in-place instead.
#        """
#        i = len(nums) - 2
#        for i in range(len(nums) - 2, -1, -1):
#            if nums[i + 1] > nums[i]:
#                for j in range(len(nums) - 1, i, -1):
#                    if nums[j] > nums[i]:
#                        break
#                print(i, j)
#                nums[i], nums[j] = nums[j], nums[i]
#                i += 1
#                j = len(nums) - 1
#                while i < j:
#                    nums[i], nums[j] = nums[j], nums[i]
#                    i += 1
#                    j -= 1
#                return
#        j = len(nums) - 1
#        while i < j:
#            nums[i], nums[j] = nums[j], nums[i]
#            i += 1
#            j -= 1