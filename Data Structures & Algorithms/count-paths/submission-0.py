
import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #m + n choose m

        return math.comb(m+n-2, m-1)

