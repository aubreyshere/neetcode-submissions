class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        maxp = len(s)

        for center in range(maxp):
            p1 = center - 1
            p2 = center + 1

            # check for odd
            while p1 > -1 and p2 < maxp:
                if s[p1] != s[p2]:
                    break
                else:
                    p1 -= 1
                    p2 += 1
                    count += 1
            count += 1
            
            # check for even
            p1 = center
            p2 = center + 1
            while p1 > -1 and p2 < maxp:
                if s[p1] != s[p2]:
                    break
                else:
                    p1 -= 1
                    p2 += 1
                    count += 1
        
        return count
        