import heapq

class MedianFinder:

    def __init__(self):
        self.items = 0
        self.maxSize = 0
        self.maxHeap = []
        self.minSize = 0
        self.minHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        self.items += 1
        if not self.maxHeap or num < -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
            self.maxSize += 1
        else:
            heapq.heappush(self.minHeap, num)
            self.minSize += 1

        if self.minSize > self.maxSize:
            swap = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -swap)
            self.maxSize += 1
            self.minSize -= 1
        elif self.minSize + 1 < self.maxSize:
            swap = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -swap)
            self.maxSize -= 1
            self.minSize += 1
        

    def findMedian(self) -> float:
        if self.items % 2:
            return -self.maxHeap[0]
        print(-self.maxHeap[0])
        print(self.minHeap[0])
        return (-self.maxHeap[0] + self.minHeap[0]) / 2
        
        