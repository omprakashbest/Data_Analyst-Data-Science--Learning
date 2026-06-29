#Qno.1: Using Binary Searching for finding the x square...O(log n)<- time complexity

class Solution:

    @staticmethod
    def my_sqrt(x):
        if x < 2:
            return x # 0 or 1 is it's own square root
        
        start = 1
        end = x // 2
        while start <= end:
            mid = start + (end - start) // 2
            # square = mid * mid
            
            if mid**2 == x:
                return mid
            elif mid**2 < x:
                start = mid + 1
            else:
                end = mid - 1   
        return end
    
print(Solution.my_sqrt(75392))