class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        jumps = [x[:] for x in [[0] * 10] * 10]
        visited = [False] * 10
        jumps[1][3] = 2
        jumps[3][1] = 2
        jumps[4][6] = 5
        jumps[6][4] = 5
        jumps[7][9] = 8
        jumps[9][7] = 8
        
        jumps[1][7] = 4
        jumps[7][1] = 4
        jumps[2][8] = 5
        jumps[8][2] = 5
        jumps[3][9] = 6
        jumps[9][3] = 6
        
        jumps[1][9] = 5
        jumps[9][1] = 5
        jumps[3][7] = 5
        jumps[7][3] = 5
        res = 0
        res += helper(1, 1, m, n, jumps, visited, 0) * 4
        res += helper(2, 1, m, n, jumps, visited, 0) * 4
        res += helper(5, 1, m, n, jumps, visited, 0)
        return res
        
        
def helper(cur, length, m, n, jumps, visited, res):
    if length >= m:
        res += 1
    length += 1
    if length > n:
        return res
    visited[cur] = True
    for nxt in range(1, 10):
        jmp = jumps[cur][nxt]
        if not visited[nxt] and (visited[jmp] or jmp == 0):
            res = helper(nxt, length, m, n, jumps, visited, res)
    visited[cur] = False
    return res