from collections import deque
class Solution:
    # dfs: for every gate (i.e. rooms[x][y] = 0) do a dfs
    #   serach until the distance from the current gate 
    #   is greater than value stored in the current location
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms or not rooms[0]:
            return rooms
        m, n = len(rooms), len(rooms[0])
        q = deque()
        dirX = [-1, 0, 1, 0]
        dirY = [0, -1, 0, 1]
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append(i * n + j)
        
        while q:
            cur = q.popleft()
            i, j = cur // n, cur % n
            for k in range(len(dirX)):
                x, y = cur // n + dirX[k], cur % n + dirY[k]
                if not 0 <= x < len(rooms) or \
                    not 0 <= y < len(rooms[0]) or \
                    rooms[x][y] < rooms[i][j] + 1:
                    continue
                rooms[x][y] = rooms[i][j] + 1
                q.append(x * n + y)
                
                        
                    
    # dfs: for every gate (i.e. rooms[x][y] = 0) do a dfs
    #   serach until the distance from the current gate 
    #   is greater than value stored in the current location
#    def wallsAndGates(self, rooms: List[List[int]]) -> None:
#        """
#        Do not return anything, modify rooms in-place instead.
#        """
#        if not rooms or not rooms[0]:
#            return rooms
#        m, n = len(rooms), len(rooms[0])
#        for i in range(m):
#            for j in range(n):
#                if rooms[i][j] == 0:
#                    dfs(rooms, i, j, 0)
#
#def dfs(rooms, x, y, dist):
#    if not 0 <= x < len(rooms) or \
#        not 0 <= y < len(rooms[0]) or \
#        rooms[x][y] < dist:
#        return
#    rooms[x][y] = dist
#    dfs(rooms, x - 1, y, dist + 1)
#    dfs(rooms, x + 1, y, dist + 1)
#    dfs(rooms, x, y - 1, dist + 1)
#    dfs(rooms, x, y + 1, dist + 1)
        