class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = { '}' : '{', ']' :'[', ')' : '('} 
        charsLeft = 0

        for char in s:
            if char in mapping:
                if charsLeft > 0:
                    value = stack.pop()
                    charsLeft -= 1
                    if value == mapping[char]:
                        continue
                return False
            else:
                stack.append(char)
                charsLeft += 1

        if len(stack) > 0:
            return False

        return True