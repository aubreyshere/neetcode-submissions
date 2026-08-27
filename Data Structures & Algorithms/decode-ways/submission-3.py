class Solution:
    def numDecodings(self, s: str) -> int:
        sing, doub = 1, 0
        i = 0
        length = len(s)

        while i < length:
            if s[i] == "0":
                return 0

            if i + 1 < length and ((1 == int(s[i]) and -1 < int(s[i+1]) < 10) or (2 == int(s[i]) and -1 < int(s[i+1]) < 7) ) :
                if not int(s[i+1]):
                    doub = 0
                    i += 1
                else:
                    temp = sing
                    sing = sing + doub
                    doub = temp
            else:
                sing = sing + doub
                doub = 0
            i += 1

        return sing + doub