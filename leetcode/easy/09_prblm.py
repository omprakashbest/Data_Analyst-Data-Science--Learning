#Add to Array-form of integer 
# The array-form of an integer nums is array representing it's digits in left to right order :- for num = 1321, the array form is [1,3,2,1].
# Given nums, the array-form of an integer , and an integer k, return the array-form of the integer num + k.

class Solution:
    def AddTo_Array_form(self, nums, k):
        nums.reverse()
        i = 0
        while k:
            digit = k % 10 # digit is nothing but the remainder number of k 
            if i < len(nums):
                nums[i] += digit
            else:
                nums.append(digit)
            
            carry = nums[i] // 10
            nums[i] = nums[i] % 10

            k = k // 10
            k += carry
            i += 1
        nums.reverse()
        return nums
    

sol  = Solution()
sol.AddTo_Array_form([3, 4, 5, 6], 34)