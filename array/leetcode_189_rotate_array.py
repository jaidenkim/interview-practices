from typing import List


class Solution:
    """https://leetcode.com/problems/rotate-array/description/"""

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        real_rotate_num = k % len(nums)
        if real_rotate_num == 0:
            return nums
        for _ in range(real_rotate_num):
            nums.insert(0, nums.pop(-1))
