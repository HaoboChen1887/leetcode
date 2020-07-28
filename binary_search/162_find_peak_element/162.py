class Solution:
    # binary search find which side to goto by looking for increasing direction
    # iterate until find the local max or until left == right
#    def findPeakElement(self, nums: List[int]) -> int:
#        nums.append(-sys.maxsize)
#        nums.insert(0, -sys.maxsize)
#        left, right = 1, len(nums) - 2
#        while left < right:
#            mid = left + (right - left) // 2
#            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
#                return mid - 1
#            elif nums[mid] < nums[mid + 1]:
#                left = mid + 1
#            elif nums[mid] < nums[mid - 1]:
#                right = mid - 1
#        return right - 1

    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return right
