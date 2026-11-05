class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures) # track (temp, index)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackVal, stackIdx = stack.pop()
                answer[stackIdx] =  i - stackIdx

            stack.append((temp, i))

        return answer