from typing import List


class Solution:
    """https://leetcode.com/problems/first-missing-positive/
    * constraints(no sorting):
        - O(n) time complexity (linear tim)
        - O(1) extra space (in-place)
    """

    def firstMissingPositive(self, nums: List[int]) -> int:
        """O(n), O(n)"""
        length = len(nums)
        filled_nums = [False] * (length + 1)
        # check whether the number is exists
        for n in nums:
            if 0 < n <= length:
                filled_nums[n] = True

        # iterate and find the smallest positive integer
        for i in range(1, length + 1):
            if not filled_nums[i]:
                return i
        return i + 1
