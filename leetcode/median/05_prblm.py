"""
-> Number fo closed Island :

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.
"""

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set() 

        def dfs(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS):
                return 0 # False
            if grid[r][c] == 1 or (r, c) in visit:
                return 1 # True
            
            visit.add((r, c))
            return min(dfs(r + 1, c),
                       dfs(r, c + 1),
                       dfs(r - 1, c),
                       dfs(r, c - 1))

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if not grid[r][c] and (r, c) not in visit:
                    res += dfs(r, c)
        return res
    
sol = Solution()

grid = [
 [1,1,1,1],
 [1,0,0,1],
 [1,0,0,1],
 [1,1,1,1]
]
print(sol.closedIsland(grid))