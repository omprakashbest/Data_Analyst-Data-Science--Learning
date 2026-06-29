# Q: Greatest Common Divisor of Strings

# for two strings s and t, we say "t divides s" if and only if s= t+t+t...+t+t (i.e, t is concatenated with
# itself one or more times.)
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

"""
Example:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # check if concatenation of both strings in different order is same or not.
        len1, len2 = len(str1), len(str2) # get length of both strings.

        def isDivisor(L): # function to check if substring of length L is divisor of both strings.
            if len1 % L or len2 % L: # if length of any string is not multiple of L, return False.
                return False
            fact1, fact2 = len1 // L, len2 // L # get how many times substring of length L can fit in both strings.
            return str1[:L] * fact1 == str1 and str1[:L] * fact2 == str2 # check if substring repeated fact1 and fact2 times gives original strings.

        for L in range(min(len1, len2), 0, -1): # iterate from min length to 1.

            # helper function to check if substring of length L is divisor of both strings.
            if isDivisor(L): # check if L is divisor of both strings.
                return str1[:L] # return the substring of str1 from 0 to L.
            return "" # if no common divisor found, return empty string.
        
# Time Complexity: O(N * M) where N and M are lengths of str1 and str2 respectively.
# Space Complexity: O(1) as we are using constant space.

# Example usage:
solution = Solution()
print(solution.gcdOfStrings("ABCABC", "ABC"))  # Output: "ABC"