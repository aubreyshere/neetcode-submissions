class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        size = len(matrix)

        #flip
        for i in range((size + 1) // 2):
            for j in range(size):
                temp = matrix[i][j]
                matrix[i][j] = matrix[size-1-i][j]
                matrix[size-1-i][j] = temp

        #transpose
        for i in range(size):
            for j in range(i+ 1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        
        