class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # using index 0
        rows = {}
        cols = {}
        squares = {}

        # set up dictionaries
        for i in range(9):
            rows[i] = set()
            cols[i] = set()
            squares[i] = set()

        # traverse through board to find invalid placements
        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val != ".":
                    if val in rows[r] or val in cols[c] or val in squares[(r // 3) + (c // 3) * 3]:
                        return False

                    rows[r].add(val)
                    cols[c].add(val)
                    squares[(r // 3) + (c // 3) * 3].add(val)
                                  
        return True        