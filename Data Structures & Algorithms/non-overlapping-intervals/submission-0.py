class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        answer = 0
        prevMax = float("-inf")

        for interval in intervals:
            low = interval[0]
            high = interval[1]

            if low < prevMax:
                answer += 1
                prevMax = min(high, prevMax)
            else:
                prevMax = high
            
        return answer
        