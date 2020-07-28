class Solution:
    # use a dp array to store the possible sequence
    # use binary search to locate where num should be inserted
    # if right > len(dp), append num to the end of dp
    # else replace dp[right] with num
    # Note: the final result in dp is not necessarily a valid sequence, but the length is correct
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            left, right = 0, len(dp)
            while left < right:
                mid = left + (right - left) // 2
                if dp[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            if right == len(dp):
                dp.append(num)
            else:
                dp[right] = num
        return len(dp)
            