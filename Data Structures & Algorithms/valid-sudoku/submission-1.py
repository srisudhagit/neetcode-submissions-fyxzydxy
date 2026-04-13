class Solution:
    def isRowValid(self, row, matrix):
        valid = set()
        for i in range(9):
            ele = matrix[row][i]
            if ele == ".":
                continue
            if ele in valid:
                return False
            valid.add(ele)
        return True

    def isColValid(self, col, matrix):
        valid = set()
        for i in range(9):
            ele = matrix[i][col]
            if ele == ".":
                continue
            if ele in valid:
                return False
            valid.add(ele)
        return True

    def issubBoxValid(self, row, col, matrix):
        valid = set()
        for i in range(row, row+3):
            for j in range(col, col+3):
                ele = matrix[i][j]
                if ele == ".":
                    continue
                if ele in valid:
                    return False
                valid.add(ele)
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        isValid = True
        for i in range(0,9):
            isValid = isValid and self.isRowValid(i, board)
        
        if not isValid:
            return False

        for j in range(0,9):
            isValid = isValid and self.isColValid(j, board)

        if not isValid:
            return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                isValid = isValid and self.issubBoxValid(i,j, board)
                
                if not isValid:
                    return False

        return True
        
        
        