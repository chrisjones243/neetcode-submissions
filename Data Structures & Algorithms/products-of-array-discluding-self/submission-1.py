from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n: int = len(nums)
        result: List[int] = [0] * n

        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in  range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result

        # for i, num in enumerate(nums):
        #     left_sum = prod(nums[:i])
        #     right_sum = prod(nums[i + 1:]) if i + 1 < n else 1

        #     out[i] = left_sum * right_sum

        # return out

