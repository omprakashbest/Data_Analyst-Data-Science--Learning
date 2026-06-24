"""
-> Find Peak Element

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. if the array contains multiple
peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. You must write an algorithm that runs in O(log n) time.

"""
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            # left neighbor greater 
            if m > 0 and nums[m] < nums[m - 1]:
                r = m - 1

            # right neighbor greater 
            elif m < len(nums) - 1 and nums[m] > nums[m + 1]:
                l = m + 1
            else:
                return m