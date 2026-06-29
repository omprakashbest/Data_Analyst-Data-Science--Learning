"""
-> Number of Zero-Filled Subarrays 

Given an integer array nums, return the number of subarrays filled with 0.

A Subarray is a contiguous non-empty sequence of elements within an array.

"""
class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        res, count = 0, 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                count = 0
            res += count 
        return res
    
# Example usage:
sol = Solution()
print(sol.zeroFilledSubarray([1,3,0,0,2,0,0,4]))  # Output: 6