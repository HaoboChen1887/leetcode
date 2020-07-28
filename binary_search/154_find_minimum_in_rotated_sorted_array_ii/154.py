class Solution:
    # use binary search, on every iteration, go to the side which is out of order
    # determine which side is out of order by compareing nums[mid] with nums[right]
    # can't compare with nums[left] because nums[mid] may equal to nums[left]
    # finally find the min
    
    # Note: the difference from find_minimum_in_rotated_sorted_array is this problem allow duplicates
    # this results in cases where nums[mid] == nums[right], in such case the previous method can't tell
    # which side is out of order
    # To solve this problem, we move the right pointer until nums[mid] != nums[right]
    # or until left < right, in which case, nums[right] is the min
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[left] <= nums[mid] < nums[right]:
                return nums[left]
            elif nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1
        return nums[right]