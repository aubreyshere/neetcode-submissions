class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals.sort(key=lambda x: x[0])        
        answer = []
        low = intervals[0][0]
        high = intervals[0][1]

        for interval in intervals:
            if high < interval[0]:
                answer.append([low, high])
                low = interval[0]
                high = interval[1]
            else:
                high = max(high, interval[1])
            

        answer.append([low, high])

        return answer    