class Solution:
#    def rob(self, nums: List[int]) -> int:
#        if not nums:
#            return 0
#        dp, p, pp = nums[0], nums[0], 0
#        for i in range(1, len(nums)):
#            dp = max(p, pp + nums[i])
#            pp, p = p, dp
#        return dp
    
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        return max(helper(nums, 1, len(nums) - 1), helper(nums, 0, len(nums) - 2))
    
def helper(nums, s, e):
    n = e - s + 1
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = nums[s]
    for i in range(2, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[s + i - 1])
    return dp[-1]