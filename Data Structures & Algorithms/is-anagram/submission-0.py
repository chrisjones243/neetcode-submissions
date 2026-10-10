class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_arr = list(s)
        t_arr = list(t)


        s_arr.sort()
        t_arr.sort()

        if s_arr == t_arr:
            return True
        return False