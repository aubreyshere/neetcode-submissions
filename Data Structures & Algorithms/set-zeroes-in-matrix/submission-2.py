class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowsZ = set()
        colsZ = set()
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                if not matrix[row][col]:
                    rowsZ.add(row)
                    colsZ.add(col)

        for row in rowsZ:
            for c in range(cols):
                matrix[row][c] = 0
        
        for col in colsZ:
            for r in range(rows):
                matrix[r][col] = 0