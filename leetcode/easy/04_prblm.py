# Concatenation of Array
#   Qno.4:- Given and integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for   0 <= i < n (0-indexed).?

class Solution:
    def getConcatenation(self, nums):
        ans = []  # Initialize empty list to store result
        
        # Loop twice to duplicate the array
        for i in range(2):  # Repeat twice to concatenate nums with itself
            # Copy all elements from nums to ans
            for n in nums:  # Go through each element in nums
                ans.append(n)  # Add element to ans
                
        return ans  # Return the concatenated array

# Example: nums = [1,2,3] -> ans = [1,2,3,1,2,3]

