import sys

def selectionSort(nums):
    for i in range(len(nums)):
        mi = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[mi]:
                mi = j
        nums[i], nums[mi] = nums[mi], nums[i]
        print(nums)

if __name__ == "__main__":
    nums = list(map(int, sys.stdin.readline().strip().split()))
    selectionSort(nums)
    print(nums)
    

