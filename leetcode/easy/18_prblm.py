"""
Q: Find the Difference Between Two Arrays.

-> Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
    - answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
    - answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

Note that the integers in the lists may be returned in any order.
"""

class Solution :
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1set , nums2set = set(nums1), set(nums2)
        res1, res2 = set(), set() # empty sets to store the results

        for n in nums1:
            if n not in nums2set:
                res1.add(n)

        for n in nums2:
            if n not in nums1set:
                res2.add(n)

        return [list(res1), list(res2)]
        