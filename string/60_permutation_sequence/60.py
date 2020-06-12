class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = []
        nums = list('123456789')
        f = [1] * n
        k -= 1
        for i in range(1, n):
            f[i] *= i * f[i - 1]
        for i in range(n, 0, -1):
            idx = k // f[i - 1]
            k %= f[i - 1]
            res.append(nums[idx])
            nums.remove(nums[idx])
        return ''.join(res)