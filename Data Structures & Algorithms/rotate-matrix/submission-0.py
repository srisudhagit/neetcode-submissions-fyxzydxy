class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        
        # step-1 reverse the matrix 180 degrees
        for col in range(cols):
            i, j = 0, rows-1
            while i <= j:
                matrix[i][col], matrix[j][col] = matrix[j][col], matrix[i][col]
                i += 1
                j -= 1

        # step-2 transpose the matrix in step-1
        for i in range(rows):
            for j in range(i, cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        