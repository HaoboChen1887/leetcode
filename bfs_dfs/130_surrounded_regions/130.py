class Solution:
    # first check through all edges, if it is a 'O' bfs all 'O's connected to it
    # mark them as '$' along the way
    # Flip all remaining 'O's to 'X's, flip all '$'s back to 'O's
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return board
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i == 0 or i == m - 1 or j == 0 or j == n - 1):
                    dfs(board, i, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '$':
                    board[i][j] = 'O'
                    
def dfs(board, i, j):
    if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] == 'X' or board[i][j] == '$':
        return
    board[i][j] = '$'
    dfs(board, i - 1, j)
    dfs(board, i + 1, j)
    dfs(board, i, j - 1)
    dfs(board, i, j + 1)
                    