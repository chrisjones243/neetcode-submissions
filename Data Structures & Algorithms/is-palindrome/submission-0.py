class Solution:
    def isPalindrome(self, s: str) -> bool:

        stack = list(filter(str.isalnum, s.lower()))
        s = list(filter(str.isalnum, s.lower()))

        i = 0
        while len(stack) > 0 and i < len(s):
            if stack[-1] == s[i]:
                stack.pop()
                i += 1
            else:
                return False

        return True
        