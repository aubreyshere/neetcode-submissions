class Solution:
    def climbStairs(self, n: int) -> int:
        cur, prev = 1, 0

        for i in range(n):
            temp = cur
            cur = cur + prev
            prev = temp

        return cur           