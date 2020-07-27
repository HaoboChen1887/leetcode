

def qsort(nums: list, low: int, high: int):
    if high - low > 1:
        pivot = nums[high]
        idx = low
        for i in range(idx + 1, high):
            if nums[i] < pivot:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
        nums[idx], nums[high] = nums[high], nums[idx]
        qsort(nums, low, idx - 1)
        qsort(nums, idx + 1, high)

