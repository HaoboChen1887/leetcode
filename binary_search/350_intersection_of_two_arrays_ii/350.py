from collections import defaultdict
class Solution:
    # use a map to count the occurance of numbers in one of the list
    # iterate through the other list to find intersection until the according entry in the map is 0
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = defaultdict(int)
        res = []
        for num in nums1:
            m[num] += 1
        for num in nums2:
            if num in m and m[num] > 0:
                m[num] -= 1
                res.append(num)
        return res
    
    # Follow up:
    # 1. if the array is sorted, we can use two pointers to record intersections
