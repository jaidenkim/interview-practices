class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        start_idx = 0
        end_idx = len(s)
        for t_char in t:
            if start_idx == end_idx:
                return True
            if t_char == s[start_idx]:
                start_idx += 1
        return start_idx == end_idx

    def isSubsequenceTwoPointers(self, s: str, t: str) -> bool:
        # exceptions
        if len(s) == 0:
            return True
        elif len(s) > len(t):
            return False
        # two points move along s and t
        s_idx = t_idx = 0
        while s_idx < len(s) and t_idx < len(t):
            if s[s_idx] == t[t_idx]:
                s_idx += 1
            t_idx += 1
        return s_idx == len(s)
