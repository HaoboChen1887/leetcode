class Solution:
    # since we don't know how the array is rotated, we need a special strategy to determine
    # whether we go to the left or the right when doing binary search
    # the method is compare nums[mid] with nums[right]
    # if nums[mid] < nums[right] it means the right half is in order
    # if nums[mid] >= nums[right] it means the left half is in order
    # based on the two conditions above, we need to check 
    # whether target is in the range [left:mid] or [mid:right] and chose sections accordingly
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[right]:
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target and nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
                
                
            
