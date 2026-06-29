"""
-> Successful Pairs of Spells and Potions?

You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.
"""

class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        
        potions.sort()
        res = []

        for s in spells:
            # binary search 
            l, r = 0, len(potions) - 1
            idx = len(potions) # find weakest potion(further left) that works

            while l <= r:
                m = l + (r - l) // 2
                if s * potions[m] >= success:
                    r = m - 1
                    idx = m
                else:
                    l = m + 1
            res.append(len(potions) - idx)
        return res