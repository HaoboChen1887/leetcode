class Solution:
    # use binary search twice
    # 1. find the first number >= target
    # 2. find the first number >= target + 1
    # edge cases:
    #   target is not in nums: nums[left] != target
    #   nums only contains same numbers e.g. [2, 2, 2], target is greater than 2: 
    #       left == len(nums)
    #   nums only contains same numbers e.g. [2, 2, 2], target is less than 2:
    #       nums[left] != target
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = findFirst(nums, 0, len(nums), target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        right = findFirst(nums, left, len(nums), target + 1) - 1
        return [left, right]
        
def findFirst(nums, left, right, target):
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right
