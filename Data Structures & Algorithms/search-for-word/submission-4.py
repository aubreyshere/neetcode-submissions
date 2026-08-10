class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        length = len(word)

        def traverseWords(row, col, letters) -> bool:
            if board[row][col] != word[letters]:
                return False
            if letters == length - 1:
                return True

            temp = board[row][col]
            board[row][col] = '#'

            for r, c in [(row - 1, col),(row + 1, col),(row, col - 1),(row, col + 1)]:
                if  0 <= r < rows and 0 <= c < cols and board[r][c] != '#':
                    if traverseWords(r, c, letters + 1):
                        board[row][col] = temp
                        return True

            board[row][col] = temp
            return False 

        for i in range(rows):
            for j in range(cols):
                if traverseWords(i, j, 0):
                    return True

        return False