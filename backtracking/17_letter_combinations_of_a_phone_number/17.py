class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        helper(0, digits, "", res)
        return res
        
def helper(idx, digits, path, res):
    if len(path) == len(digits):
        res.append(path)
        return
    for i in range(combLen(int(digits[idx]))):
        helper(idx + 1, digits, path + letter(int(digits[idx]), i), res)
        
def combLen(d):
    l = 4 if d == 9 or d == 7 else 3
    return l

def letter(d, i):
    if d > 7:
        i += 1
    return chr(ord('a') + (d - 2) * 3 + i)