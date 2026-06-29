#  Range Sum Query - Immutables
# Qno.7: Given an integer array nums, handle multiple queries of the following type:-
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

class Solution:
    def __init__(self, nums: list[int]): # Constructor
        self.prefix = []  # List to store prefix sums
        cur = 0  # Running total
        for i in nums:  # Go through each number in nums
            cur += i  # Add current number to running total
            self.prefix.append(cur)  # Store running total in prefix list

    def sumRange(self, left: int, right: int) -> int:
        right_Sum = self.prefix[right]  # Sum from start to 'right'
        left_Sum = self.prefix[left - 1] if left > 0 else 0  # Sum before 'left' , Using this line comprehension in python
        return right_Sum - left_Sum  # Difference gives sum from left to right


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left, right)