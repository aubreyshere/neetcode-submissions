import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid = (r + l) // 2
            time_spent = 0

            # loop that calculated timespent
            for pile in piles:
                time_spent += math.ceil(pile/mid)

            if time_spent > h:
                l = mid + 1
            else:
                res = mid
                r = mid - 1

        return res