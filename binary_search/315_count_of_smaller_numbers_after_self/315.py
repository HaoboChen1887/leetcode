class Solution:
    # construct an ordered array from the original array, starting from the last element
    # use binary search to determine where to insert(i.e. this is essentially insertion sort)
    # at the end of each iteration, the index at which the new number should be inserted
    # is the number of elements to its right that are less than itself
    def countSmaller(self, nums: List[int]) -> List[int]:
        tmp, res = [], [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            left, right = 0, len(tmp)
            while left < right:
                mid = left + (right - left) // 2
                if tmp[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            res[i] = right
            tmp.insert(right, nums[i])
        return res