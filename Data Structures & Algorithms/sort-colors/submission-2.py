class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counts: dict = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        out = []
        for i in range(0, max(nums) + 1):
            count = counts.get(i, None)
            if not count:
                continue

            for _ in range(0, count):
                out.append(i)

        for i, num in enumerate(out):
            nums[i] = out[i]


        