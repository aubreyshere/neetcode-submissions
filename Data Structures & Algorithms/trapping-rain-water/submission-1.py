class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        postfix = []
        pointer2 = len(height) - 1
        preHighest = 0
        postHighest = 0
        answer = 0

        for i in range(len(height)):
            preHighest = max(preHighest, height[i])
            postHighest = max(postHighest, height[pointer2 - i])
            prefix.append(preHighest)
            postfix.append(postHighest)

        pointer2 = len(height) - 1

        for i in range(len(height)):
            answer += min(prefix[i], postfix[pointer2 - i]) - height[i]

        return answer