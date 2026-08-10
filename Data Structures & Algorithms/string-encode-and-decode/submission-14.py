class Solution:

    def encode(self, strs: List[str]) -> str:
        answer = ""
        for word in strs:
            answer += str(len(word)) +  '#' + word
        
        return answer

    def decode(self, s: str) -> List[str]:
        answer = []

        p1 = 0
        print(s)

        while p1 < len(s):
            length = ''
            while s[p1] != '#':
                length = length + s[p1] 
                p1 += 1
            
            start = p1 + 1
            end = start + int(length)
            answer.append(s[start:end])
            p1 = end
        return answer
