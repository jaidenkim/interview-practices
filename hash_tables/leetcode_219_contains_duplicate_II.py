from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:  # 32ms, beats 21.74%
        counter = {}
        for i, n in enumerate(nums):
            if n in counter and counter[n] - i <= k:
                return True
            counter[n] = i
            if i >= k:
                counter.pop(nums[i - k])
        return False
