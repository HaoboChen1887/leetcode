class Solution:
    # first sort the enveloped by width in ascending order, 
    # in case of tie, sort by height in descending order
    # the way of breaking tie is important because 
    # we want to choose the smallest envelope possible, just by intuition
    # and the way we update dp is appending the envelope when we find a larger
    # and replacing the old one when we find a smaller one
    # if we didn't break tie in this way, in cases like [4, 5][4, 6], we would add both to the solution
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x : (x[0], -x[1]))
        dp = []
        for enve in envelopes:
            left, right = 0, len(dp)
            while left < right:
                mid = left + (right - left) // 2
                if dp[mid][1] < enve[1]:
                    left = mid + 1
                else:
                    right = mid
            if right == len(dp):
                dp.append(enve)
            else:
                dp[right] = enve
        return len(dp)
            