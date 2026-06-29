# Question: Shuffle the array
# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# return the array in the form [x1,y1,x2,y2,...,xn,yn].

class Solution(object):
    def Shuffle(self, nums: list[int], n: int) -> list[int]: # One way to solution
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i+n])
        return result


    def Shuffle2(self, nums: list[int], n: int) -> list[int]: # Another way to solution
        for i in range(n):
            nums[i] = nums[i] << 10
            nums[i] = nums[i] | nums[i+n] # store x, y in binary

        # reverse the array
        j = 2*n - 1
        for i in range(n-1, -1, -1):
            x = nums[i] & (2**10 - 1)
            y = nums[i] >> 10

            nums[j] = y
            nums[j-1] = x
            j -= 2
        return nums

