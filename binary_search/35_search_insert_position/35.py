
class Solution:
    # equivalent to finding the first number that is not less than the target
    # search result is determined by what conditions are included in the else block
    # in this case >= target
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        while low < high:
            mid = low + (high - low) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid
            else:
                low = mid + 1
        return high
        