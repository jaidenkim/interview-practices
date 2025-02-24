from typing import List


class Solution:
    """https://leetcode.com/problems/majority-element"""

    def majorityElementNaive(self, nums: List[int]) -> int:
        """use convienient data structure, map"""
        majority_criteria = len(nums) // 2 + 1  # use quotient
        cache = {}
        for n in nums:
            if n not in cache:
                cache[n] = 1
            else:
                cache[n] += 1
            if cache[n] >= majority_criteria:
                return n
        # You may assume that the majority element always exists in the array
        return

    def majorityElementNaive2(self, nums: List[int]) -> int:
        """use convienient data structure, map"""
        # You may assume that the majority element always exists in the array
        # => a number which has maximum count is a majority
        majority_value, maximum_count = 0, 0
        counts = {}
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)  # if not exists, update +1
            if counts[n] > maximum_count:
                majority_value = n
                maximum_count = counts[n]
        return majority_value

    def majorityElement(self, nums: List[int]) -> int:
        """Follow-up: Could you solve the problem in linear time and in O(1) space?"""
        # You may assume that the majority element always exists in the array
        # majority_value, count = nums[0], 1
        # for n in nums[1:]:
        #     if n != majority_value:
        #         if count > 0:
        #             count -= 1
        #         else:
        #             count += 1
        #             majority_value = n
        #     else:
        #         count += 1
        # return majority_value

        majority_value, count = 0, 0
        for n in nums:
            if count == 0:
                majority_value = n
            count += 1 if majority_value == n else -1
        return majority_value
