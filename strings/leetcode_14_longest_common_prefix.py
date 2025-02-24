from typing import List


class Solution:
    """
    * constraints:
        - strs[i] consists of only lowercase English letters if it is non-empty.
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        start_idx = 0
        num_strs = len(strs)
        min_strs_len = len(strs[0])
        for s in strs[1:]:
            min_strs_len = min(len(s), min_strs_len)

        # exception
        if min_strs_len == 0:
            return ""

        lcp = ""
        while start_idx < min_strs_len:
            char = ""
            is_break = False
            for i in range(num_strs):
                if i == 0:
                    char = strs[i][start_idx]
                    continue
                if char != strs[i][start_idx]:
                    is_break = True
                    break
                char = strs[i][start_idx]

            if is_break:
                break

            lcp += char
            start_idx += 1

        return lcp
