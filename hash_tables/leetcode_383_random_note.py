class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:  # 35 ms, Beats 9.54%
        """Each letter in magazine can only be used once in ransomNote."""
        if len(ransomNote) > len(magazine):
            return False
        counter = {}
        r_len = len(ransomNote)
        for i in range(len(magazine)):
            if i < r_len:
                r = ransomNote[i]
                if r in counter:
                    counter[r] += 1
                else:
                    counter[r] = 1
            m = magazine[i]
            if m in counter:
                counter[m] -= 1
            else:
                counter[m] = -1
        return max(counter.values()) <= 0
