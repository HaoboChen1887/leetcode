class Solution:
    # use single iterations of quicksort to quickly locate the kth largest value
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        while True:
            pos = partition(nums, left, right)
            if pos == k - 1:
                return nums[pos]
            if pos > k - 1:
                right = pos - 1
            else:
                left = pos + 1
            
        
    
def partition(nums, left, right):
    pivot = nums[right]
    idx = left
    for i in range(left, right):
        if nums[i] > pivot:
            nums[i], nums[idx] = nums[idx], nums[i]
            idx += 1
    nums[right], nums[idx] = nums[idx], nums[right]
    return idx
    
       