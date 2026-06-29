"""
Removing Stars from a String ?

You are given a string s, which contains stars *.
In one operation,

you can remove the closest non-star character to the left of a star, as well as remove the star itself.
Return the string after all stars have been removed.

"""

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        for ch in s :
            if ch == "*":
                stack and stack.pop() # check if stack is not empty first.
            else:
                stack .append(ch)
        return "".join(stack)
            
