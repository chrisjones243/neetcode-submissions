class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low, high = 0, len(nums) - 1

        while low <= high:
            pivot = low + (high - low) // 2

            if target < nums[pivot]:
                high = pivot - 1
            elif target > nums[pivot]:
                low = pivot + 1
            else:
                return pivot
            
        return -1
