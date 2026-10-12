class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        max_length = 0
        left = 0

        for i, c in enumerate(s):
            while c in seen:
                seen.remove(s[left])
                left += 1
                
            seen.add(c)
            max_length = max(max_length, i - left + 1)

        return max_length

