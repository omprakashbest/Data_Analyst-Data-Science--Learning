""" 
Minimize Maximum of Array

You given a 0 -indexed array nums comprising of n non- negative integers.
In one operation, 

you can choose an index i such that 1 <= i < n and nums[i] > 0,
then decrease nums[i] by 1 and increase nums[i - 1] by 1.

Return the minimum possible value of the maximum integer of nums after performing any number of operations.

"""
import math

class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        res = total = nums[0]

        for i in range(1, len(nums)):
            total += nums[i]
            res = max(res, math.ceil(total / (i + 1)))
        return res