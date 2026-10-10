class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = list(filter(str.isalnum, s.lower()))
        stack = s.copy()

        i = 0
        while len(stack) > 0 and i < len(s):
            if stack[-1] == s[i]:
                stack.pop()
                i += 1
            else:
                return False

        return True