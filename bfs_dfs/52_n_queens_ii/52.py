class Solution:
    res = 0
    def totalNQueens(self, n: int) -> List[List[str]]:
        queenCol = [-1] * n
        self.helper(0, queenCol)
        return self.res
    
    # use recursion to enumerate all possible locations
    # when we get a valid solution on the last row, we can add it to res
    def helper(self, curRow, queenCol):
        n = len(queenCol)
        if curRow == n:
            self.res += 1
            return

        for i in range(n):
            if isValid(queenCol, curRow, i):
                queenCol[curRow] = i
                self.helper(curRow + 1, queenCol)
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