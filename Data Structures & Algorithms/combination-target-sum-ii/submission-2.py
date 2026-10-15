class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        subset = []

        candidates.sort()

        def dfs(i, total):

            if total == target:
                results.append(subset.copy())
                return

            if total > target or i >= len(candidates):
                return

            # Choose to add it
            subset.append(candidates[i])
            dfs(i + 1, total + candidates[i])

            # Choose not to add it
            subset.pop()

            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1

            dfs(j, total)

        dfs(0, 0)
        return results