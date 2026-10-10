class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []

        for i, cur_num in enumerate(nums):
            cur_nums = nums.copy()
            cur_nums.pop(i)

            left = 0
            right = len(cur_nums) - 1

            while left < right:
                total = cur_num + cur_nums[left] + cur_nums[right]

                if total == 0:
                    out = sorted([cur_num, cur_nums[left], cur_nums[right]])

                    if out not in result:
                        result.append(out)

                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
        
        return list(result)