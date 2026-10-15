class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        subset = []

        def dfs(i):
            total = sum(subset)

            if total == target:
                results.append(subset.copy())
                return

            if total > target or i >= len(nums):
                return

            # We add itself
            subset.append(nums[i])
            dfs(i)

            # We don't add itself, and move on
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return results