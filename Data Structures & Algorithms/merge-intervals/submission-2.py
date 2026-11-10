class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        length = len(intervals)

        if length < 2:
            return intervals

        answer = []
        intervals.sort(key=lambda x:x[0]) # O(n logn)
        start = 0
        cur = 1
        high = intervals[0][1]

        while cur < length:
            if intervals[cur][0] > high:
                answer.append([intervals[start][0], high])
                start = cur

            high = max(intervals[cur][1], high)
            cur += 1

        answer.append([intervals[start][0], high])    

        return answer
