"""
Optimal Partition of String 

-> Given a string s, partition the string into one or more substring such that the characters in each substring
are unique. that is, no letter appears in a single substring more than once.

Return the minimum number of substring in such a partition.

Note -> that each character should belong to exactly one substring in a partition.
"""


class Solution:
    def partitionString(self, s: str) -> int:
        curSet = set()
        res = 1

        for c in s:
            if c in curSet:
                res += 1
                curSet = set()
                curSet.add(c)
            else:
                curSet.add(c)
        return res
