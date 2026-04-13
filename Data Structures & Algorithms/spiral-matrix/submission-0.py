class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        output = []

        while top <= bottom and left <= right:
            for i in range(left, right+1):
                output.append(matrix[top][i])
            top += 1

            for j in range(top, bottom+1):
                output.append(matrix[j][right])
            right -= 1

            if not (left <= right and top <= bottom):
                break
                
            for k in range(right, left-1, -1):
                output.append(matrix[bottom][k])
            bottom -= 1

            for l in range(bottom, top-1, -1):
                output.append(matrix[l][left])
            left += 1
        
        return output

            
        