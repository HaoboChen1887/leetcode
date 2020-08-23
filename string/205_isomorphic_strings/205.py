from collections import defaultdict
class Solution:
    # use 2 maps two record where each letters occurs in two strings
    # if the last idx occured is different then they are not isomorphic
    # NOTE: we update map by i + 1 because we need to distinguish 
    # between the initial conditio where everything is 0
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1, m2 = [0] * 256, [0] * 256
        for i in range(len(s)):
            if m1[ord(s[i])] != m2[ord(t[i])]:
                return False
            m1[ord(s[i])] = i + 1
            m2[ord(t[i])] = i + 1
        return True