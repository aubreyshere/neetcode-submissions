class Solution:
    def maxArea(self, heights: List[int]) -> int:
        pointer1 = 0
        pointer2 = len(heights) - 1

        answer = 0

        while pointer1 < pointer2:
            length = pointer2 - pointer1
            if heights[pointer1] <= heights[pointer2]:
                answer = max(answer, heights[pointer1] * length)
                pointer1 += 1
            elif heights[pointer1] > heights[pointer2]:
                answer = max(answer, heights[pointer2] * length)
                pointer2 -= 1
        
        return answer

        