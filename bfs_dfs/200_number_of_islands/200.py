from collections import deque
class Solution:
    # bfs: maintain a visited matrix, for every location that is not water and is not visited
    #   increase count and do a bfs search, bfs is implemented by a queue
    #   start search from the current location, append top, bottom, left, right to the queue
    #   check boundary, whether it is visited, whether it is water
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        res = 0
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for i in range(m)]
        dirX = [-1, 0, 1, 0]
        dirY = [0, -1, 0, 1]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0' or visited[i][j]:
                    continue
                res += 1
                q = deque([i * n + j])
                while q:
                    t = q.popleft()
                    for k in range(len(dirX)):
                        x = t // n + dirX[k]
                        y = t % n + dirY[k]
                        if not 0 <= x < m or not 0 <= y < n or visited[x][y] or grid[x][y] == '0':
                            continue
                        visited[x][y] = True
                        q.appendleft(x * n + y)
        return res
        
    # dfs: maintain a visited matrix, for every location that is not water and is not visited
    #   increase count and do a dfs search, dfs is implemented by recursion, 
    #   recursion would return until it reaches the end of the path
    #   when it returns to the outer function, a complete island has been explored
#    def numIslands(self, grid: List[List[str]]) -> int:
#        if not grid or not grid[0]:
#            return 0
#        
#        res = 0
#        m, n = len(grid), len(grid[0])
#        visited = [[False] * n for i in range(m)]
#        for i in range(m):
#            for j in range(n):
#                if grid[i][j] == '0' or visited[i][j]:
#                    continue
#                else:
#                    dfs(grid, visited, i, j)
#                res += 1
#        return res
#    
#def dfs(grid, visited, i, j):
#    if not 0 <= i < len(grid) or \
#        not 0 <= j < len(grid[0]) or \
#        visited[i][j] or grid[i][j] == '0':
#        return
#    visited[i][j] = True
#    dfs(grid, visited, i - 1, j)
#    dfs(grid, visited, i + 1, j)
#    dfs(grid, visited, i, j - 1)
#    dfs(grid, visited, i, j + 1)
    