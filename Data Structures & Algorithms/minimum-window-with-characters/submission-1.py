class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = {}
        charsLeft = len(t)
        maxWindow = len(s)
        left = 0
        shortestString = ""

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
                if shortestString == "" or len(shortestString) > index + 1 - left:
                    shortestString = s[left:index + 1]

                if s[left] not in count:
                    pass
                elif count[s[left]] < 0:
                    count[s[left]] += 1
                else:
                    count[s[left]] += 1
                    charsLeft += 1
                
                left += 1

        return shortestString

                
        
                

        
            