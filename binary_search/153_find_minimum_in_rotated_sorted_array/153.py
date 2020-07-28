class Solution:
    # use binary search, on every iteration, go to the side which is out of order
    # determine which side is out of order by compareing nums[mid] with nums[right]
    # can't compare with nums[left] because nums[mid] may equal to nums[left]
    # finally find the min
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[left] <= nums[mid] < nums[right]:
                return nums[left]
            elif nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[right]