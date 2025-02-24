from typing import List


class Solution:
    """https://leetcode.com/problems/move-zeroes/description/"""

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        current_idx = 0
        for _ in range(len(nums)):
            if nums[current_idx] == 0:
                zero = nums.pop(current_idx)
                nums.append(zero)
            else:
                current_idx += 1
