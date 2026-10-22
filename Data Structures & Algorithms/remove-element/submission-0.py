class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp: List[int] = []
        for i, num in enumerate(nums):
            if num != val:
                tmp.append(num)
            
        for i in range(0, len(tmp)):
            nums[i] = tmp[i]

        return len(tmp)
        