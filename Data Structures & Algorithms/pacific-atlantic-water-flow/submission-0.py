class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacificReachable = set()
        atlanticReachable = set()
        visted = set()
        rows = len(heights)
        cols = len(heights[0])

        def oceanExtend(r: int, c: int, ocean) -> None:
            if (r, c) in ocean:
                return

            ocean.add((r,c))
            val = heights[r][c]

            if 0 < r and heights[r - 1][c] >= val:
                oceanExtend(r - 1, c, ocean)
            if r < rows - 1 and heights[r + 1][c] >= val:
                oceanExtend(r + 1, c, ocean)
            if 0 < c and heights[r][c - 1] >= val:
                oceanExtend(r, c - 1, ocean)
            if c < cols - 1 and heights[r][c + 1] >= val:
                oceanExtend(r, c + 1, ocean)


        for c in range(cols):
            oceanExtend(0, c, pacificReachable)
            oceanExtend(rows - 1, c, atlanticReachable)
            
        for r in range(rows):
            oceanExtend(r, 0, pacificReachable)
            oceanExtend(r, cols - 1, atlanticReachable)

        answer = []
        for i in range(rows):
            for j in range(cols):
                if (i,j) in pacificReachable and (i,j) in atlanticReachable:
                    answer.append([i, j])

        return answer


        