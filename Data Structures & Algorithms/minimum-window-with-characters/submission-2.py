class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = {}
        charsLeft = len(t)
        left = 0
        bestl = -1
        bestr = -1

        for char in t:
            count[char] = 1 + count.get(char, 0)

        for index in range(len(s)):
            if s[index] not in count:
                continue
            elif count[s[index]] <= 0:
                count[s[index]] -= 1
            else:
                count[s[index]] -= 1
                charsLeft -= 1

            while charsLeft == 0:
                if bestl == -1 or bestr - bestl > index - left:
                    bestl = left
                    bestr = index

                if s[left] not in count:
                    pass
                elif count[s[left]] < 0:
                    count[s[left]] += 1
                else:
                    count[s[left]] += 1
                    charsLeft += 1
                
                left += 1

        if bestl == -1:
            return ""
        else:
            return s[bestl:bestr + 1]

                
        
                

        
            