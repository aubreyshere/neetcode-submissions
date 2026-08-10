class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        tracker = []
        result = []

        for num in nums:
            try:
                count[num] += 1
            except:
                count[num] = 1

        for num, freq in count.items():
            tracker.append([freq, num])
        
        tracker.sort(reverse=True)

        for item in range(k):
            result.append(tracker[item][1])
        
        return result


        
        
        