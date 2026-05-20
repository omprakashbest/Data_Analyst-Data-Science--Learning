"""
Minimum Score of a Path Between two cities

->  You are given a positive integer n representing n cities numbered from 1 to n, You are also given a 2D array 
roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi
with a distance equal to distancei. the cities graph is not necessarily connected.

The score of a path between two cities is defined as the minimum distance of a road in this path.

Return the minimum possible score of a path between cities 1 and n.

Note:

• A path is a sequence of roads between two cities.
• It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple 
    times along the path.
• The test cases are generated such that there is at least one path between 1 and n.

"""

class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        adj = defaultdict(list) # type: ignore # node -> list of (neighbor, distance)
        for src, dst, dist in roads:
            adj[src].append((dst, dist))
            adj[dst].append((src, dist))
        
        def dfs(i):
            if i in visit:
                return 
            visit.add(i)
            nonlocal res
            for neigh, dist in adj[i]:
                res = min(res, dist)
                dfs(neigh)
        
        res = float("inf") # infinity
        visit = set()
        dfs(1)
        return res
    
        