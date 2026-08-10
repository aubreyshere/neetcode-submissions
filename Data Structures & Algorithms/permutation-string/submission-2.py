class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        left = 0
        lettersLeft = len(s1)

        for letter in s1:
            count[letter] = 1 + count.get(letter, 0)

        for right in range(len(s2)):
            if s2[right] not in count:
                while left < right:
                    count[s2[left]] += 1
                    left += 1
                left = right + 1
                lettersLeft = len(s1)

            elif count[s2[right]] != 0:
                count[s2[right]] -= 1
                lettersLeft -= 1

            else:
                while count[s2[right]] == 0:
                    count[s2[left]] += 1
                    left += 1
                    lettersLeft += 1
                
                count[s2[right]] -= 1
                lettersLeft -= 1
            
            if lettersLeft == 0:
                return True


        return False



