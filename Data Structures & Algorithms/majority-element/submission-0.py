class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
            
        set_count: dict = {}

        for num in nums:
            set_count[num] = set_count.get(num, 0) + 1

        freq = [(-count, num) for num, count in set_count.items()]
        
        heapq.heapify(freq)
        
        return freq[0][1]
