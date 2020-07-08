import sys
from collections import deque
from random import random

def mergesort(nums):
    if len(nums) < 2:
        return deque(nums)
    mid = len(nums) // 2
    left = mergesort(nums[:mid])
    right = mergesort(nums[mid:])
    res = deque()
    while left and right:
        if left[0] <= right[0]:
            res.append(left.popleft())
        else:
            res.append(right.popleft())
    if left:
        res += left
    if right:
        res += right
    return res

def test():
    for i in range(10):
        for l in range(int(random() * 100 // 1)):
            nums = [0] * l
            for i in range(l):
                nums[i] = int(random() * 100 // 1)
        ans = deque(sorted(nums))
        res = mergesort(nums)
        print(res)
        print(ans == res)

if __name__ == '__main__':
    nums = list(map(int, sys.stdin.readline().strip().split()))
    res = mergesort(nums)
    print(res)
    print(res == deque(sorted(nums)))
    test()

