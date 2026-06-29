"""
-> Number of Enclaves :

You are given a mxn binary matrix grid, where 0 represent a sea cell and 1 represent a land cell.

A move consist of walking form one land cell to another adjacent (4-directionally) land cell or walking off
the boundary of the grid.

return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number 
of moves.
"""

class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0]) # number of rows and columns in the grid

        # return num of land cells in the current island.
        def dfs(r, c):
            # base case: if we are out of bounds or we are on a sea-cell or we have already visited this land cell, then we return 0.
            if (r < 0 or c < 0 or r == ROWS or c == COLS or not grid[r][c] or (r, c) in visit):
                return 0
            
            visit.add((r, c)) # mark the current land cell as visited
            res = 1 # count the current land cell
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # (down, up, right, left)
            for dr, dc in directions:
                res += dfs(r + dr, c + dc)
            return res
        
        visit = set() # hashset to store visited land cells
        land, border_land = 0, 0

        for r in range(ROWS):
            for c in range(COLS):
                land += grid[r][c]
                if (grid[r][c] and (r, c) not in visit and (c in [0, COLS - 1] or r in [0, ROWS - 1])):
                    border_land += dfs(r, c)
        return land - border_land


grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
sol = Solution()
print(sol.numEnclaves(grid))
