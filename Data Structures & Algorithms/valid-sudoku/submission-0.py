class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # go thru each item check if col if row and if box
        colSets = []
        colCount = []
        squareSets = []
        squareCount = []
        rowIndex = 0

        # create sets and counters for each column and square
        for num in range(9):
            colSets.append(set())
            colCount.append(0)
            squareSets.append(set())
            squareCount.append(0)

        # iterate through each item and add to lists
        for row in board:
            rowItems = set()
            rowCount = 0
            colIndex = 0

            for item in row:

                if item != ".":
                    rowCount += 1
                    rowItems.add(item)
                    colCount[colIndex] += 1
                    colSets[colIndex].add(item)
                    squareIndex = (rowIndex // 3) * 3 + (colIndex // 3)
                    squareCount[squareIndex] += 1
                    squareSets[squareIndex].add(item)
                
                colIndex += 1
        
            rowIndex += 1
            if rowCount != len(rowItems):
                return False
        
        # validate answer
        for i in range(9):
            if len(colSets[i]) != colCount[i]:
                return False
            if len(squareSets[i]) != squareCount[i]:
                return False
        
        return True

