from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:  # 0ms, beats 100%
        number2idx = {}
        cnt = 0
        for i, n in enumerate(nums):
            if n in number2idx:
                cnt += len(number2idx[n])
                number2idx[n].append(i)
            else:
                number2idx[n] = [i]
        return cnt
