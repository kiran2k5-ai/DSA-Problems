from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])

        firstcol = any(matrix[i][0] == 0 for i in range(rows))
        firstrow = any(matrix[0][j] == 0 for j in range(cols))

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if firstrow:
            for j in range(cols):
                matrix[0][j] = 0

        if firstcol:
            for i in range(rows):
                matrix[i][0] = 0
