class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-1 * stone for stone in stones]

        heapq.heapify(maxHeap)
        
        while len(maxHeap) >= 2:
            big_stone = heapq.heappop(maxHeap)
            smaller_stone = heapq.heappop(maxHeap)

            big_stone -= smaller_stone

            if big_stone < 0:
                heapq.heappush(maxHeap, big_stone)
        
        if len(maxHeap) == 0:
            return 0

        return maxHeap[0] * -1