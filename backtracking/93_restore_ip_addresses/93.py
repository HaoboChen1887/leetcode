class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        helper(s, res, [])
        return list(set(res))

def helper(remain, res, tmp):
    if len(tmp) == 3 and len(remain) > 3:
        return
    if len(tmp) == 4 and not remain:
        res.append('.'.join(tmp))
    for i in range(min(3, len(remain))):
        if int(remain[:i + 1]) > 255 or str(int(remain[:i + 1])) != remain[:i + 1]:
            return
        
        helper(remain[i + 1:], res, tmp + [(remain[:i + 1])])