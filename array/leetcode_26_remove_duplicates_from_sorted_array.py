from typing import List


class Solution:
    """https://leetcode.com/problems/remove-duplicates-from-sorted-array/
    * condition:
        - in-place
        - keep relative order
    * constraint:
        - `nums` is in non-decreasing order
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        current_idx = 0
        for _ in range(len(nums)):
            if current_idx == 0:
                start_num = nums[current_idx]
                current_idx += 1
                continue

            curr_num = nums[current_idx]
            if start_num == curr_num:
                nums.pop(current_idx)
            else:
                start_num = curr_num
                current_idx += 1
        return len(nums)
