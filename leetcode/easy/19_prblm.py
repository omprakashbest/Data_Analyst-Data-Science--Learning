"""
Matrix Diagonal Sum :

Given a square matrix 'mat', return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal
that are not part of the primary diagonal.

"""

class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        res, n = 0, len(mat)

        for i in range(n):
            res += mat[i][i] # primary diagonal
            res += mat[i][len(mat)-1-i] # secondary diagonal

        return res - (mat[n // 2][n // 2] if n % 2 else 0)