class Solution:
    def isPalindrome(self, s: str) -> bool:
        pointer1 = 0
        pointer2 = len(s) - 1

        while pointer1 < pointer2:
            while not s[pointer1].isalnum() and pointer1 < pointer2:
                pointer1 += 1
            while not s[pointer2].isalnum() and pointer1 < pointer2:
                pointer2 -= 1

            val1, val2 = s[pointer1].lower(), s[pointer2].lower()
            if val1 != val2:
                return False

            pointer1 += 1
            pointer2 -= 1
        
        return True
        