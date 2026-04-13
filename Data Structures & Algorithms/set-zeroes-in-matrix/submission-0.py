class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        firstRowZero = any(matrix[0][i] == 0 for i in range(cols))
        firstColumnZero = any(matrix[i][0] == 0 for i in range(rows))

        # flag
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # fill
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if firstRowZero:
            for j in range(cols):
                matrix[0][j] = 0

        if firstColumnZero:
            for i in range(rows):
                matrix[i][0] = 0
            

        
        