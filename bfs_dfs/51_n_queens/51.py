class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        queenCol = [-1] * n
        helper(0, queenCol, res)
        return res
    
# use recursion to enumerate all possible locations
# when we get a valid solution on the last row, we can add it to res
def helper(curRow, queenCol, res):
    n = len(queenCol)
    if curRow == n:
        path = [''.join(['.'] * n) for _ in range(n)]
        for i in range(n):
            path[i] = path[i][:queenCol[i]] + 'Q' + path[i][queenCol[i] + 1:]
        res.append(path)
        return
    
    for i in range(n):
        if isValid(queenCol, curRow, i):
            queenCol[curRow] = i
            helper(curRow + 1, queenCol, res)
            queenCol[curRow] = -1
            
# to be valid, there has to be no queen on the same row, same column and on the diagonals
# because we use a 1-D array to store the queens, it has already guaranteed 
# there is only one queen on each row
# so we have to check on previous rows, whether there are queens on the same column as the current queen
# to check the diagonals, we can compare if abs(x1 - x2) == abs(y1 - y2)
def isValid(queenCol, row, col):
    for i in range(row):
        if queenCol[i] == col or abs(i - row) == abs(queenCol[i] - col):
            return False
    return True