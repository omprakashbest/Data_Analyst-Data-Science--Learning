# Contains Duplicate ||
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

class Solution(object):
    # Naive solution using brute force O(n^2)
    def contain_Duplicate(self, nums, k) -> bool: # return type is boolean
        # Check every pair of elements
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # If values are equal and indices are within k distance
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
        return False
    

    # Efficient solution using sliding window and hash set (O(n))
    def contain_Duplicate2(self, nums:list[int], k:int) -> bool: # return type is boolean
        
        window = set()  # Store unique elements in the current window
        left = 0        # Left pointer for the window
        
        for right in range(len(nums)):
            # Keep window size at most k
            if right - left > k:
                window.remove(nums[left])  # Remove element going out of window
                left += 1

            # If current element already in window, duplicate found
            if nums[right] in window:
                return True
            window.add(nums[right])  # Add current element to window
        return False
