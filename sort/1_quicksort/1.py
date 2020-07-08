import sys
from random import random

def qsort(nums, low, high):
    if low < high:
        pivot = nums[high]

        idx = low
        for i in range(low, high):
            if nums[i] < pivot:
                nums[i], nums[idx] = nums[idx], nums[i]
                idx += 1
        
        nums[high], nums[idx] = nums[idx], nums[high]

        qsort(nums, low, idx - 1)
        qsort(nums, idx + 1, high)

def test():
    for i in range(10):
        for l in range(int(random() * 100 // 1)):
            nums = [0] * l
            for i in range(l):
                nums[i] = int(random() * 100 // 1)
        ans = sorted(nums)
        qsort(nums, 0, len(nums) - 1)
        print(nums)
        print(ans == nums)


if __name__ == '__main__':
    nums = list(map(int, sys.stdin.readline().strip().split()))
    ans = sorted(nums)
    qsort(nums, 0, len(nums) - 1)
    print(nums)
    print(ans == nums)
    test()

