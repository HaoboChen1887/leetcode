# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    # binary search, when updating high we use mid instead of mid + 1 
    # because the answer may be skipped if it happens to be the mid
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        while low < high:
            mid = (high - low) // 2 + low
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low