class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencies = {}

        for num in nums:
            frequencies[num] = frequencies.get(num, 0) - 1

        heap: List[(int, int)] = list(frequencies.items())

        # Swap around num, count
        for i, (num, count) in enumerate(heap):
            heap[i] = (count, num)

        heapq.heapify(heap)

        out: List[int] = []
        while k > 0:
            most_freq: int = heapq.heappop(heap)[1]
            out.append(most_freq)
            k -= 1

        return out
        # freq_to_nums = {}

        # for num, freq in frequencies.items():
        #     if freq not in freq_to_nums:
        #         freq_to_nums[freq] = []
        #     freq_to_nums[freq].append(num)

        # result = []

        # for freq in range(len(nums), 0, -1):
        #     if freq in freq_to_nums:
        #         for num in freq_to_nums[freq]:
        #             result.append(num)

        #         if len(result) == k:
        #             return result

        # return result

        