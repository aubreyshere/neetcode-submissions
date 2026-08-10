class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        def removeIsland(i: int, j: int) -> None:
            if not (0 <= i < rows and 0 <= j < cols) or grid[i][j] == "0":
                return

            grid[i][j] = "0"
            removeIsland(i+1, j)
            removeIsland(i-1, j)
            removeIsland(i, j+1)
            removeIsland(i, j-1)



        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != "0":
                    removeIsland(i, j)
                    islands += 1

        return islands
        