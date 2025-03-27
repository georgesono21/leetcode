class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        """
        i feel like this is very straightforward. just check the rows and columns,
        and then check every 3x3 box for that constraint.

        """
        #valid rows and columns

        #O(n^2)
        for i in range(9):
            rowVals = set()
            colVals = set()
            for j in range(9):
                if board[i][j] in rowVals:
                    return False
                
                if board[j][i] in colVals:
                    return False

                if board[i][j] != ".":
                    rowVals.add(board[i][j])
                if board[j][i] != ".":
                    colVals.add(board[j][i])
    
        # cords = [(0,0), (0,3), (0,6)]

        #O(n^2)
        for i in range(0,9,3):
            for j in range(0,9,3):
                boxVals = set()
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        if board[x][y] in boxVals:
                            return False
                        if board[x][y] != ".":
                            boxVals.add(board[x][y])
                        

        return True