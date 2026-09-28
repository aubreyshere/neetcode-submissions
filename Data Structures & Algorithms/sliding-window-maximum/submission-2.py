import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        answer = []

        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        answer.append(-heap[0][0])

        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], i))

            while True:
                top = heapq.heappop(heap)

                if top[1] > i - k:
                    break
            
            heapq.heappush(heap, top)
            answer.append(-top[0])

        return answer
        