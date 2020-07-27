
def mergeSort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    l = mergeSort(nums[:mid])
    r = mergeSort(nums[mid:])

    res = []
    while l and r:
        if l[0] < r[0]:
            res.append(l.pop(0))
        else:
            res.append(r.pop(0))
    
    if l:
        res += l
    if r:
        res += r

    return res

