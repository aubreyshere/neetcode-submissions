class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        offset = 0

        for i in range(n+1):
            if offset * 2 == i or not offset:
                offset = i
            
            if not offset:
                answer.append(0)
            else:
                answer.append(answer[i - offset] + 1)
        return answer