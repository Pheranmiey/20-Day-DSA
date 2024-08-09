Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]

Output
[null, null, null, 1.5, null, 2.0]

class MedianFinder:

    def __init__(self):
        # Max-Heap (inverted to use as a max-heap)
        self.low = []
        # Min-Heap
        self.high = []
    
    def addNum(self, num: int) -> None:
        # Add to max-heap (low)
        heapq.heappush(self.low, -num)
        
        # Balance the heaps (ensure every element in low <= every element in high)
        if self.low and self.high and (-self.low[0] > self.high[0]):
            heapq.heappush(self.high, -heapq.heappop(self.low))
        
        # Rebalance sizes
        if len(self.low) > len(self.high) + 1:
            heapq.heappush(self.high, -heapq.heappop(self.low))
        elif len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))
    
    def findMedian(self) -> float:
        # If the number of elements is odd, return the middle element
        if len(self.low) > len(self.high):
            return -self.low[0]
        # If the number of elements is even, return the average of the two middle elements
        return (-self.low[0] + self.high[0]) / 2
        
