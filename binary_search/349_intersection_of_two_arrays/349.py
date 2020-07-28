class Solution:
    # sort one of the array, iterate through the other array and search in the other array
    # use set to remove duplicates
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        keys, search = [nums1, nums2] if len(nums1) < len(nums2) else [nums2, nums1]
        search.sort()
        res = set()
        for key in keys:
            if key in res:
                continue
            elif key == binarySearch(search, key):
                res.add(key)
        return res
            
def binarySearch(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return target
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return -1