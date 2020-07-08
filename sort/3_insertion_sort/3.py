import sys

def insertionSort(nums):
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
            else:
                break



if __name__ == '__main__':
    nums = list(map(int, sys.stdin.readline().strip().split()))
    insertionSort(nums)
    print(nums)

