# Count odd Number in an Interval Range
# Given two non-negative integer low and high. return the count of odd numbers between low and high (inclusive).
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Calculate total numbers in range (including both endpoints)
        length = high - low + 1
        
        # Most numbers will have half odd, half even
        count = length // 2
        
        # If total count is odd AND starting number is odd, add one more
        # This handles cases like [3,4,5,6,7] where we have 3 odd numbers
        if length % 2 != 0 and low % 2 != 0:
            count += 1
            
        return count


sol = Solution()
print(sol.countOdds(3, 7))  # Should print 3 (odd numbers: 3, 5, 7)

